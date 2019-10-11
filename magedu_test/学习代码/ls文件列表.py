import argparse, stat
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser(prog='ls', # 定义功能名称
                                 description='list information about the files',    # 功能描述
                                 add_help=False  # -h功能是否开启
                                 )
parser.add_argument('path', # 添加位置参数及名称
                    nargs='*',  # '?'：可选参数可有可无，+：至少一个，*：任意个，数字：参数个数
                    default='.',    # 缺省路径
                    help='path help'    # 该参数帮助信息
                    )
parser.add_argument('-l',   # 添加选项参数及名称
                    dest='list',
                    # nargs='?' -> [-l [L]] 不是我们想要的
                    action='store_true',   # 这里用action，-l有设定则返回true，否则返回false
                    # action='store_const  const=20 表示：-l有设定则返回20，否则返回none
                    help='use a long listing format'
                    )
parser.add_argument('-a',   # 添加选项参数及名称
                    '--all',    # 定义长选项名称
                    action='store_true',
                    help='do not ignore entries starting with .'
                    )
parser.add_argument('-h',
                    dest='human',
                    action='store_true',
                    help='with -l, print sizes in human readable format (e.g. 1k 234M 2G)'
                    )

def listdir(path:list, all=False, list=False, human=False):
    # 定义函数，获取文件属性
    def getmode(mode: int, symbol='rwxrwxrwx'):
        tar_str = ''
        for index, i in enumerate(range(8, -1, -1)):
            if mode >> i & 1:
                tar_str += symbol[index]
            else:
                tar_str += '-'
        return tar_str
    # 定义函数，获取文件类型
    def gettype(file: Path):
        if file.is_symlink():
            return 'l'
        elif file.is_socket():
            return 's'
        elif file.is_char_device():
            return 'c'
        elif file.is_fifo():
            return 'p'
        elif file.is_block_device():
            return 'b'
        elif file.is_dir():
            return 'd'
        else:
            return '-'
    # 定义函数，文件大小处理
    def getsize(size: int, symbol=' KMGTP'):
        index = 0
        while size > 1000:
            size //= 1000
            index += 1
        return str(size) + symbol[index].rstrip(' ')
    # 定义函数，获取路径下的文件,属性，大小，属组，时间，路径，文件名称
    def _listdir(path:list, all=False, list=False, human=False):
        for i in path:  # 当path参数设定为可接受任意参数时，args.path返回一个列表，这时需要进行迭代处理
            p = Path(i)
            for file in p.iterdir():    # 迭代path路径下的文件
                if not all and file.name.startswith('.'):   # 根据-a参数，判断是否显示以.开头的文件
                    continue
                if list:    # 根据-l参数，判断是否详细显示文件路径
                    filestat = file.stat()
                    # mode = gettype(file) + getmode(filestat.st_mode) # 文件类型-rwxrwxrwx处理
                    mode = stat.filemode(filestat.st_mode)  # stat.filemode标准模块处理
                    atime = datetime.fromtimestamp(filestat.st_atime).strftime('%Y/%m/%d %H:%M:%S') # 时间戳处理，并格式化
                    size = getsize(filestat.st_size) if human else filestat.st_size # 根据-h参数，判断如何显示文件大小格式
                    yield (mode, filestat.st_uid, filestat.st_gid, size, atime, file.name)
                else:
                    yield (file.name,)
    yield from sorted(_listdir(path, all, list, human), key=lambda x: x[-1])    # 按照文件名称排序

if __name__ == '__main__':

    args = parser.parse_args()  # 分析参数，参数为可迭代类型
    # parser.print_help() # 打印帮助
    # print(args) # 打印收集到的参数
    # print(args.all, args.list, args.path)   # 打印定义过的参数数据
    for i in listdir(args.path, args.all, args.list, args.human):
        print(i)

# uid、gid的转换
# import grp, pwd
# pwd.getpwuid(Path()).stat().st_uid).pw_name
# grp.getgrgid(Path()).stat().st_gid).gr_name
# pathlib模块，Path().group() Path().owner()


