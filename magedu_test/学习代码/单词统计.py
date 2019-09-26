
# 对一个文件中的单词进行统计，不区分大小写，并显示单词重复最多的10个单词
from collections import defaultdict

def makekey(src:str, chars = '''\n`~!@#$%^&*()_+- "'=:{}[];|\<>,.?/'''):
    start = 0
    # 切片
    for i,char in enumerate(src):
        if char in chars:
            if start == i:  # 如果字符开始时就是特殊字符，则start已经等于i
                start += 1  # start需要加等，并continue
                continue
            yield src[start:i]
            start = i + 1   # 跳过特殊字符
    else:
        if start < len(src):    # 小于则说明字符末尾未切完
            yield src[start:]

def topn(n:int, filename:str):
    # 缺省字典
    tar_dict = defaultdict(lambda :0)
    # tar_dict = {}

    # 以utf-8编码打开文件
    with open(filename, encoding='utf-8') as f:
        # 以行读取
        for line in f:
            # 函数切片
            for word in map(str.lower, makekey(line)):  # map,revers都是惰性求值，并且转小写
                # tar_dict[word] = tar_dict.get(word, 0) + 1  # 一般字典get方法，如果get不到，则返回缺省值0
                tar_dict[word] += 1  # 缺省字典用法

    # yield前n个
    yield from sorted(tar_dict.items(), key=lambda x:x[1], reverse=True)[:n]
    # yield from sorted(tar_dict.items(), key=lambda x:x[1], reverse=True)


print(list(topn(5, 'sample.txt')))










