import datetime, time, random, threading
from queue import Queue

# 数据源
def data_src():
    while True:
        yield {'value': random.randint(1, 100),
               'datetime': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))}
        time.sleep(1)

# 数据处理(求平均数)
def handler(buff):
     return sum(map(lambda x:x['value'], buff)) / len(buff)

# 窗口函数
def window(src:Queue, handler, width, interval):
    '''
    窗口函数
    :param src: 数据源
    :param handler: 数据处理函数
    :param width: 截取时间宽度
    :param interval: 间隔时间
    :return:
    '''
    start_time = datetime.datetime.strptime('20170101 000000 +0800', '%Y%m%d %H%M%S %z')
    current_time = datetime.datetime.strptime('20170101 000000 +0800', '%Y%m%d %H%M%S %z')
    dalta_time = datetime.timedelta(seconds=width - interval)
    buffer = []
    while True: # 不停的处理数据，那么用死循环
        # 从数据源中获取数据
        data = src.get() # 从queue中get数据
        if data:
            buffer.append(data)
            current_time = data['datetime'] # 每次数据获取，重新刷新当前数据时间

        # 窗口截取数据（当启动时间>=时间间隔）====>间隔截取数据，间接数据缓冲
        if (current_time - start_time).total_seconds() >= interval:
            ret = handler(buffer)
            print('{:.2f}'.format(ret), threading.current_thread())
            start_time = current_time   # 每次处理完一批数据后，更新数据开始时间

            # 清除过期数据
            buffer = [x for x in buffer if x['datetime'] > current_time - dalta_time]

# 分发器
def dispatcher(src):
    handlers = []   # 记录注册过的handler
    queues = [] # 记录注册过的queue（队列）
    # 注册函数
    def reg(handler, width, inerval):
         q = Queue()    # 建立新的queue
         queues.append(q)

         h = threading.Thread(target=window, args=(q, handler, width, inerval)) # 建立新的线程，并调用window函数
         handlers.append(h)

    def run():
        for h in handlers:
            h.start()  # 启动进程

        for data in src:    # 先获取数据源，然后分发到队列中
            for q in queues:
                q.put(data)

    return reg, run

reg, run = dispatcher(data_src())

reg(handler, 10, 5)
reg(handler, 8, 4)
print(threading.current_thread())
run()
