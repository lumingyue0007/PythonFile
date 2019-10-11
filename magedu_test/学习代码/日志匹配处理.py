
# 一般处理方式，练习相关知识 *************************************************************
import re
from datetime import datetime

# line = '''123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] "GET / HTTP/1.1" 200 8642 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'''

def makekey(src:str):
    chars = ' []"'
    start = 0
    flag = False
    for i,c in enumerate(src):
        if c in chars:
            if c == '[':    # 用[做标记，遇到]的时候，关闭标记，这样就可以直接截取到：[06/Apr/2017:18:09:25 +0800]
                start = i + 1
                flag = True
            elif c == ']':
                flag = False
            elif c == '"':  # 用"做标记，因为"无法区分左右，所以直接用"进行标记，直接获取："GET / HTTP/1.1"
                flag = not flag
                if flag:
                    start = i + 1
            if flag: continue
            if start == i:  # 当连续出现需要跳过的字符时，处理方法
                start += 1
                continue
            yield src[start:i]
            start = i + 1
    else:   # 当字符结束时，start没有到达字符串尾部，则需截取剩余部分
        if start < len(src):
            yield src[start:]
# 定义字典key
names = ('remote', '', '', 'datetime', 'request', 'status', 'length', '', 'useragent')
# 对字典的每个value进行处理，比如时间，请求，状态，大小
ops = ('None', 'None', 'None',
       lambda timestr: datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z').__str__(),    # __str__()显示格式
       lambda request: dict(zip(('method', 'url', 'protocol'), request.split())),
       int, int, 'None', 'None'
       )
# 行处理
def extract(line:str):
    # 先用zip将names，makekey，ops依次匹配，组成每个元素为三元组的元组
    # 然后用map将每个元素（每个元素包括三个元素）取出，用lambda判断第三个元素是否为函数，如果是函数则用该函数对第二元素处理，如果是none，则返回第二个元素（不处理）
    # 最后用dict包装输出
    return dict(map(lambda item: (item[0], item[1] if item[2] == 'None' else item[2](item[1])), zip(names, makekey(line), ops)))

with open('test.log', 'r', encoding='utf8') as f: # 文件打开的一种方式 while
    line = f.readline()
    while line:
        print(extract(line))
        line = f.readline()


# 使用正则表达式匹配方式   ***********************************************************************
import re, datetime
src = '''112.64.118.97 - - [06/Apr/2017:19:13:59 +0800] "GET /favicon.ico HTTP/1.1" 200 4101 "-" "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G9250 Build/LMY47X)"'''

def extract(src:str):
    # 定义一个k与函数对应的字典
    ops = {'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z').__str__(),
           'status': int, 'size': int}
    # 定义正则表达
    pattern = '(?P<remote>[\d\.]{7,15}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<method>[^" ]+) (?P<url>[^" ]+)' \
              ' (?P<protocol>[^" ]+)" (?P<status>\d+) (?P<length>\d+) "[^"]+" "(?P<useragent>[^"]+)"'
    regex = re.compile(pattern)
    matcher = regex.match(src)
    if matcher:
        # 重新生成一个字典，get方法并使用默认缺省
        return  {k: ops.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}
    else:
        return src  # 异常处理

def load(filename:str):
    with open(filename, encoding='utf8') as f:  # 文件打开，注意编码格式
        for line in f:  # 文件处理一般都是行处理
            fields = extract(line)
            if isinstance(fields, (dict,)):
                yield fields
            else:
                # 匹配异常打印输出
                print('no match. {}'.format(fields))

for x in load('test.log'):
    print(x)






