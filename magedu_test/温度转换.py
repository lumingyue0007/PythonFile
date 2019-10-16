
# 实现温度处理

# 思路，一般需求：输入一个温度值和单位，输出其他两类温度
# 类属性访问

class Temp:
    def __init__(self, temp, unit='c'):
        if unit == 'c':
            self.f = temp * 9 / 5 + 32
            self.k = temp + 273.15
            self.c = temp
        elif unit == 'k':
            self.c = temp - 273.15
            self.f = self.c * 9 / 5 + 32
            self.k = temp
        else:
            self.f = temp
            self.c = (temp - 32) * 5 / 9
            self.k = self.c + 273.15

T = Temp(30, 'f')
print(T.c, T.k, T.f)
