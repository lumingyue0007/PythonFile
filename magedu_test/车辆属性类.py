
# 记录车的品牌，颜色，价格，速度等特征，不实现增加车辆信息，显示全部车辆信息的功能

# 定义类，增加单一车辆信息属性
class Car:
    def __init__(self, mark, color, price, speed):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed

    def __repr__(self): # 字符串显示
        return '<{} {} {} {}>'.format(self.mark, self.color, self.price, self.speed)

# 定义类，增加车辆，以及显示车辆信息
class CarInfo:
    carinfo = []

    def addcar(self, car:Car):
        self.carinfo.append(car)

    def getallcarinfo(self):
        return self.carinfo

# 新增单一车辆信息
car = Car('audi', 'red', 20, 200)

# 把单一车辆信息增加到车辆信息库里
carinfo = CarInfo()
carinfo.addcar(car)
carinfo.addcar(car)
print(carinfo.getallcarinfo())

