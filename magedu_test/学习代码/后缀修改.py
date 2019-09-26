# 写一个脚本实现找到/tmp目录及其子目录下的以.htm结尾的文件，把其后缀名改为.html
from pathlib import Path
# 方法一：给定一个文件夹，将文件夹下的内容迭代判断，是文件夹的进入到该文件夹，再次判断
p = Path('Temp')

def fn(p):
    # 迭代目录内的内容
    for x in p.iterdir():
        # 判断是否是文件夹
        if x.is_dir():
            # 路径拼接，递归
            p = p.joinpath(x.name)
            fn(p)
            # 路径复位
            p = p.parent
        else:
            # 匹配文件后缀类型，并修改后缀
            if x.match('*.tmp'):
                x.rename(x.with_suffix('.html'))

fn(p)

# 方法二：要求给定路径
p = Path('test2/a')

def fn(p, ret=[], i=1):
    if i == 1:
        for x in p.iterdir():
            if x.match('*.xml'):
                x.rename(x.with_suffix('.temp'))
            ret.append(x.name)
        i += 1
    for x in p.parents[len(p.parents)-i].iterdir():
        if x.is_dir():
            # print(x)
            i += 1
            if i <= len(p.parents):
                fn(p, i=i, ret=ret)
        else:
            if x.match('*.xml'):
                x.rename(x.with_suffix('.temp'))
                ret.append(x.name)
    return ret



