
# 查找list中出现次数最多的元素，并显示该元素出现的次数  ***********************************************

a = [1,2,3,4,2,3,1,2,1,2,2]
print(max(set(a),key=a.count))

from collections import Counter
cnt = Counter(a)
print(cnt.most_common(1))


# 通过itertools里边的permutations函数生成给定可迭代的对象的所有排序组合，看以下例子   ************************************

from itertools import permutations
print(list(permutations([1, 2, 3])))
# ==> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

#其可以接收第二个参数r， 指定生成对象的长度，默认与所传可迭代对象长度一致

from itertools import permutations
print(list(permutations([1, 2, 3], 2)))
# ==> [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 之前就有介绍过内置的zip函数的作用，其将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,然后返回由这些元组组成的列表，先看个zip的例子： ******************************

a = [1, 2, 3]
b = ['a', 'b']
list(zip(a, b)) # ===>  [(1, 'a'), (2, 'b')]

# zip返回的长度取决于参数中长度最短的。下面介绍下itertools中的zip_longest，先看个例子：

from itertools import zip_longest
a = [1, 2, 3]
b = ['a', 'b']
list(zip_longest(a, b)) # ===> [(1, 'a'), (2, 'b'), (3, None)]
#可见zip_longest返回的长度等于参数中长度最大的，对于缺失的项用None填充。

合并列表（extend）
       跟元组一样，用加号（+）将两个列表加起来即可实现合并：
x=list(range(1, 13, 2))
x + ['b', 'a']

       对于已定义的列表，可以用extend方法一次性添加多个元素：
x2=[3, 6, 1]
x.extend(x2)
x

隐藏特性 1，函数unpack
def foo(x, y):
	print x, y

alist = [1, 2]
adict = {'x': 1, 'y': 2}

foo(*alist) # 1, 2

foo(**adict) # 1, 2










