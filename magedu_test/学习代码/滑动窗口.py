import random, datetime, time
# 数据源，产生数据和时间
def source():
    while True:
        # 该数据产生的时间，不带时区，后面计算的时候，要注意，建议在该部分加上时区
        # yield {'value':random.randint(1, 100), 'datetime':datetime.datetime.now()}
        yield {'value':random.randint(1, 100),
               'datetime':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
               }
        time.sleep(1)

# 数据处理函数，送入一批数据，计算一个结果(计算平均值)
def handler(data):
    return sum(map(lambda x: x['value'], data)) / len(data)

# 窗口函数
def window(src_data, function, width:int, interval:int):
    '''
    窗口函数
    :param src_data: 数据源，生成器，用来生成数据
    :param function: 数据处理函数
    :param width: 时间窗口宽度，秒
    :param interval: 处理时间间隔，秒
    :return:
    '''
    start = datetime.datetime.strptime('20170101 000000 +0800', '%Y%m%d %H%M%S %z')
    current = datetime.datetime.strptime('20170101 000000 +0800', '%Y%m%d %H%M%S %z')
    buffer = [] # 缓存待处理的数据
    delta = datetime.timedelta(seconds=width - interval)    # 注意时间，width-interval是个int数，而后面比较是时间比较

    while True:
        # 从数据生成器中，获取数据，并缓冲
        data = next(src_data)
        if data:
            buffer.append(data) # 数据临时缓冲等待计算
            current = data['datetime']

        # 使用窗口从buffer中获取并计算数据
        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            print('{:.2f}'.format(ret))
            start = current
            print([i['value'] for i in buffer])

            # 清除超出width的数据(过期数据)
            buffer = [x for x in buffer if x['datetime'] > current - delta]
            print([i['value'] for i in buffer])

window(source(), handler, 10, 5)

