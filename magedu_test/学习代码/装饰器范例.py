import functools
# 函数装饰器===>装饰函数
def logger(fn):
    @functools.wraps(fn)
    def _logger(*args, **kwargs):
        ret = fn(*args, **kwargs)
        return ret
    return _logger

@logger # add = logger(add)
def add(x, y):
    return x + y

print(add(1, 4))
print(add.__name__)

# 类装饰器====>装饰类，为类增加一个属性
def add_name(name):
    def _add_name(cls):
        cls.name = name
        return cls
    return _add_name

@add_name('tom')   # Person = add_name(Person)
class Person:
    age = 10

a = Person()
print(a.age)
print(a.name)

# 类装饰器，为类增加一个方法
def add_shut(cls):
    def _shut(self):
        print('{} shut'.format(type(self).__name__))
    cls.shut = _shut
    return cls

@add_shut   # Animal = add_shut(Animal)
class Animal:
    age = 5
b = Animal()
print(b.age)
b.shut()


