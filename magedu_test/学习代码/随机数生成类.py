import random
# 随机生成一批数，可以指定范围，可以指定个数
class RandomGen:
    def __init__(self, start=1, stop=100, count=10):
        self.start = start
        self.stop = stop
        self.count = count

    def generater(self):
        return [random.randint(self.start, self.stop) for _ in range(self.count)]

# 将上述的随机数，两两组成坐标
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = [Point(x, y) for x,y in zip(RandomGen().generater(), RandomGen().generater())]

for i in points:
    print(i.x, i.y)