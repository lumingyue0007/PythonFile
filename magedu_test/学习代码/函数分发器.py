# 命令分发器，程序员可以方便的注册函数到某一个命令，用户输入命令时，路由到注册的函数，如果此命令没有对应的注册函数，执行默认函数

# 思路：首先要求注册函数，然后在注册函数内找，找到后直接读取注册内的函数返回
def cmd_dipa():
    cmd_dict = {}
    # 注册函数，输入命令和函数名称,如果cmd已存在提示，如果不存在则创建
    def register(cmd):
        def _register(fn):
            if cmd in cmd_dict.keys():
                print('Command is exists')
            else:
                cmd_dict[cmd] = fn
            # return fn
        return _register

    # 定义一个初始函数
    def default_fn():
        print('unknown command, please register')

    # 定义一个功能，一直监控输入命令，如果命令已注册，则返回函数，否则返回初始函数
    def dispatcher():
        while True:
            cmd = input('>>>>')
            if cmd == '':
                return
            cmd_dict.get(cmd, default_fn)()  # get返回函数，所以后面加（）
    return register, dispatcher

register, dispatcher = cmd_dipa()

@register('f1')  # 函数注册
def f1():
    print('f1 '*20)

@register('f2')  # 函数注册
def f2():
    print('f2 '*20)

dispatcher()