# 将配置文件的内容，转换成json格式，并保存成文件

from configparser import ConfigParser
import json

cfg = ConfigParser()
cfg.read('test.ini')

# 带default格式输出
d = {}
for i,_ in cfg.items():
    d[i] = dict(cfg.items(i))

# 不带default格式输出
dd = {}
for section in cfg.sections():
    dd[section] = dict(cfg.items(section))

# 将json内容写入到文件中
with open('test.json', 'w') as f:
    json.dump(dd, f)

# 从文件中读取内容，并json
with open('test.json', 'r+') as f:
    read = json.load(f)

print(dd)
print(read)




















