# 判断一个数有几位，并打印  折半思想
'''
num = int(input('>>>'))
if num >= 1000:
    if num >= 10000:
        length = 5
    else:
        length = 4
else:
    if num >= 100:
        length = 3
    elif num >= 10:
        length = 2
    else:
        length = 1
print('length=', length)
'''
# 上题延续：# 从高位到低位打印
'''
avl1 = num
x = 10 ** (length-1)
for i in range(length):
    print(avl1 // x , end=' ') 
    avl1 %= x
    x //= 10
'''
# 上题延续：# 从低位到高位打印
'''
avl2 = num
for i in range(length):
    print(avl2 % 10, end=' ')
    avl2 = avl2 // 10
'''
# 判断学生成绩，成绩等级A~E.其中，90分以上的为A，80~89分的为B，70~79分的为C，60~69分的为D，60分以下的为E
'''
x = int(input('>>>'))
if x >= 90:
    y = 'A'
elif x >= 80:
    y = 'B'
elif x >= 70:
    y = 'C'
elif x >= 60:
    y = 'D'
else:
    y = 'E'
print(y)
'''
# 输出一个数，打印出以这个数为边的正方形
'''
n = int(input('>>>')) # 方法一
# 方法一
n = int(input('>>>')) 
n = int(input('>>>')) # 方法一
for i in range(n):
    if i == 0 or i == n-1:
        print('*' * n)
    else:
        print('*'+' '*(n-2)+'*')
# 方法二  对称写法
n = int(input('>>>')) 
x = -n // 2
for i in range(x, x+n):
    if i == x or i == x+n-1:
        print('*' * n)
    else:
        print('*' + ' ' * (n-2) + '*')
n = int(input('>>>')) # 方法二  对称写法
x = -n // 2
for i in range(x, x+n):
    if i == x or i == x+n-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
'''
# 1~5的阶乘之和
'''
x = 1
y = 0
for i in range(1, 6):
    x *= i
    y += x
    print(x, y)
'''
# 求100以内所有奇数的和
'''
y = 0
for i in range(1, 100, 2):
    y += i
print(y)
'''
# 给一个数，判断是否为素数 ==>素数只能被1和它本身整除
'''
n = int(input('>>>'))
for i in range(2, n):
    if n % i == 0:
        print(n, 'is not a prime number')
        break
else:
    print(n, 'is a prime number')
'''
# 给一个半径，求圆的面积和周长
'''
import math
r = float(input('>>>'))
x = math.pi * r ** 2
y = math.pi * r * 2
print(x, y)
'''
# 输入两个数，比较大小后，从小到大升序打印
'''
x = int(input('>>>1'))
y = int(input('>>>2'))
if x > y:
    print(y, x)
else:
    print(x, y)
'''
# 依次输入若干个整数，打印出最大值。如果输入为空，则退出
'''
firstnum = input('>>>')
if firstnum != '':
    print(firstnum)
    while 1:
        num = input('>>>')
        if num:
            num = int(num)
            firstnum = int(firstnum)
            if firstnum < num:
                firstnum = num
            print(firstnum)
        else:
            break
'''
# 三元表达式
'''
a = 1
b = 0
if a > b:
    print(a)
else:
    print(b)
print(a) if a > b else print(b)  # 三元表达式写法
'''
# 输入n个数，求每次输入后的算术平均数
'''
result = 0
count = 0
while 1:
    num = input('>>>')
    if num != '':
        num = int(num)
        result += num
        count += 1
        print('sum is', result)
        print('average is', result/count)
    else:
        break
'''
# 打印九九乘法表
'''
# 方法一
for i in range(1, 10):
    line = ''
    for j in range(1, i+1):
        avl = i * j
        if j > 1 and avl < 10:
            avl = str(avl) + ' '
        line = str(j) + '*' + str(i) + '=' + str(avl) + ' '
        print(line, end='')
    print()
# 方法二
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={:<{}}'.format(j, i, i * j, 1 if j < 2 else 2), end=' ')
    print()
# 方法三
for i in range(1, 10):
    for j in range(i, j+1):
        print('{}*{}={:<2}'.format(i, j, i*j), end=' ')
    print()
# 方法四
for i in range(1, 10):
    print(' '*7*(i-1), end='')
    for j in range(i, 10):
        print('{}*{}={:<2}'.format(i, j, i*j), end=' ')
    print()
# 方法五 =====> 将一行视为一个整体，然后整体右对齐
for i in range(1, 10):
    line = ''
    for j in range(i, 10):
        line += '{}*{}={:<{}}'.format(i, j, i*j, 2 if j < 4 else 3)
    print('{:>60}'.format(line))
'''
# 输入一个数，打印最长为这个数的菱形 ====> 对称，range（-3, 4）
'''
# 方法一
n = int(input('>>>'))
for i in range(-n//2+1, n//2+1):
    print(' '*abs(i) + '*'*(n-abs(i)*2))
# 方法二
n = int(input('>>>'))
e = n // 2
for i in range(-e, e+1):
    for j in range(1, n+1):
        if abs(i) < j < n-abs(i)+1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
# 方法三  ==> 坐标系思路，即：x轴和y轴的坐标值加起来，小于x或者y。但是该方式如果图形不对称，则打印不准确
n = int(input('>>>'))
e = n // 2
for x in range(-e, e+1):
    for y in range(-e, e+1):
        if abs(x) + abs(y) == e:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
# 打印对顶三角形
'''
# 方法一
n = int(input(">>>"))
e = n // 2
for i in range(-e, e+1):
    print(' ' * (e - (abs(i))) + '*' * (abs(i) * 2 + 1))
# 方法二
n = int(input(">>>"))
e = n // 2
for y in range(e, -e-1, -1):
    for x in range(-e, e+1):
        if  abs(y) >= abs(x):
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
#  打印闪电
'''
# 方法一
n = 7
for y in range(3, -4, -1):
    for x in range(-3, 4):
        if (x <= 0 <= y or y <= 0 <= x) and abs(x) + abs(y) < 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()
# 方法二
n = 7
for i in range(-3, 4):
    if i < 0:
        print(' ' * abs(i) + '*' * (4 - abs(i)))
    elif i > 0:
        print(' ' * abs(3) + '*' * (4 - abs(i)))
    else:
        print('*' * n)
'''
# 斐波那契数列：求100以内。=====> 一个数列从第三项项开始，每个数等于前两项之和
'''
x = 0
y = 1
while 1:
    fib = x + y
    if fib > 100:
        break
    print(fib)
    x, y = y, fib  # ==> x = y ; y = fib
'''
# 斐波那契数列：求第101项
'''
x = 1
y = 1
count = 2
while count < 101:
    fib = x + y
    count += 1
    x, y = y, fib  # ==> x = y ; y = fib
print(count, fib)
'''
# 求10万以内所有质数  ====> 质数：大于1的自然数，只能被1和本身整除的数
'''
# 方法一
import datetime
start = datetime.datetime.now()
l = [2]
for i in range(3, 100000, 2):  # 从3开始，剔除偶数，===》缩小范围，减少遍历
    for j in range(3, int(i**0.5) + 1, 2):  # 从3开始=》剔除偶数，因为奇数不能被偶数整除=》开方范围减半=》以防万一范围+1
        if i % j == 0:
            break
    else:
        l.append(i)
print((datetime.datetime.now() - start).total_seconds())
print(len(l))
# 方法二
lst= [2, 3]
n = 1000000
x = 5
step = 2
while x <= n:
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            break
    else:
        lst.append(x)

    x += step
    step = 4 if step == 2 else 2
# 方法三  ******************最优算法
a = [2]
for i in range(3, 1000000, 2):  # 剔除2，剔除偶数
    edge = i**0.5   # 计算耗时  ***********************************
    flag = False    # 是质数
    for j in a:  # 一个数如果能被质数整除，它一定是合数
        if i % j == 0:
            flag = True
            break
        if j > edge:  # 当j的范围超过i的开方，表示这个数一定是质数
            break
    if not flag:
        a.append(i)
print(len(a))
# 方法四 ====> 大于3的质数，及与6整数相邻的两个数关系
lst = [2, 3]
for i in range(6, 1000000, 6):
    flag1 = flag2 = flag3 = 0
    edge = i**0.5
    for j in lst:
        if (i-1) % j == 0:
            flag1 = 1
        if (i+1) % j == 0:
            flag2 = 1
        if i % j == 0:
            flag3 = 1
        if j > edge:
            # pass
            break
    if not flag1:
        lst.append(i-1)
    if not flag2:
        lst.append(i+1)
    if not flag3:
        lst.append(i)
'''
# 依次接收用户输入的3个数，排序后打印 ====四种方法
'''
# 方法一：转换int后，判断大小排序。使用分支结构
x = int(input('>>>'))
y = int(input('>>>'))
z = int(input('>>>'))
if x > y:
    if y > z:
        print(x, y, z)
    elif x > z:
        print(x, z, y)
    else:
        print(z, x, y)
else:
    if z < x:
        print(y, x, z)
    elif z < y:
        print(y, z, x)
    else:
        print(z, y, x)
# 方法一 ===== 变形
lst = []
for i in range(3):
    lst.append(int(input('{}:='.format(i))))
if lst[0] > lst[1]:
    if lst[1] > lst[2]:
        out = [0, 1, 2]
    elif lst[0] > lst[2]:
        out = [0, 2, 1]
    else:
        out = [2, 0, 1]
else:
    if lst[2] < lst[0]:
        out = [1, 0, 2]
    elif lst[2] < lst[1]:
        out = [1, 2, 0]
    else:
        out = [2, 1, 0]
for i in out:
    print(lst[i], end=' ')
# 方法二：使用列表sort方法
lis = []
for i in range(3):
    lis.append(int(input('>>>')))
lis.sort(reverse=False)
print(lis)
# 方法三：使用max函数
lst = []
for i in range(3):
    lst.append(int(input('>>>')))
s = ''
for i in range(3):
    m = max(lst)
    lst.remove(m)
    s += '{}, '.format(m)
print(s)
# 冒泡法
lst = []
for i in range(3):
    lst.append(int(input('>>>')))
length = len(lst)
for i in range(length):
    flag = 0
    for j in range(length-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            flag = 1
    if not flag:
        break
print(lst)
'''
# 冒泡方法排序,即优化提高
'''
import random
lst = list(range(10))
random.shuffle(lst)
print(lst)
length = len(lst)
for i in range(length-1):  # 循环列表长度-1次，总循环次数，（循环最后一次，是空比较，所以省略）
    flag = 0
    for j in range(length-1-i):     # 每次交换后，末尾的数就不需要比较，即每次循环后，次数-1，即-i
        if lst[j] > lst[j+1]:
            lst[j+1], lst[j] = lst[j], lst[j+1]
            flag = 1
    if not flag:    # 增加标志位，当一个循环后，没有出现数据交换，即表示数据顺序符合排序要求***************************
        break
print(lst)
'''
# 用户输入一个数字。判断该数字是几位数，依次打印每一位数及其重复的次数（顺序：个十百千万）
'''
n = input('>>>').strip().lstrip('0')     # 去除输入值前后空格，去除前0
if n.isdigit():
    print('length={}'.format(len(n)))
    cout = [0] * 10
    for i in n:
        cout[int(i)] += 1
    for i in range(1, len(n)+1):    # 倒序打印字符串，字符串看作列表
        print('{}：number={}, count={}'.format(i, n[-i], cout[int(n[-i])]))
else:
    print('input error')
'''
# 输入5个数字，打印每个数字的位数，将这些数字按升序打印
'''
a = []
for i in range(5):
    n = input('>>>').strip().lstrip('0')
    if n.isdigit():
        a.append([int(n), len(n)])
    else:
        print('input error')
a.sort(key=lambda x: x[0])      # 嵌套列表sort方法
for i in range(5):
    print('number={}, length={}'.format(a[i][0], a[i][1]))
'''
# 杨辉三角
'''
# 方法一：原有列表数据进行计算，即，新行列表=上一行列表第0和第1个元素之和，然后在新行列表左右加1，该方式打印杨辉三角所有元素
a = [[1]]
for i in range(1, 6):
    lastline = a[i-1]
    curline = [1]
    for j in range(i-1):
        curline.append(lastline[j]+lastline[j+1])
    curline.append(1)
    a.append(curline)
print(a)
# 方法二  右侧补0，等同于左右两边补0
a = [[1]]
for i in range(1, 6):
    lastline = a[i-1] + [0]     # 不改变原有列表，采用中间变量
    preline = []
    # a.append(preline)    # 放在此行也可以，表示preline为复杂元素，下面的操作变化，都是围绕复杂元素进行（浅拷贝）
    for j in range(i+1):
        preline.append(lastline[j-1]+lastline[j])
    a.append(preline)
print(a)
'''
# 求杨辉三角的第m行第k个元素
'''
# 方法一：新行列表等于上一行列表的第0和第1个元素之和，然后在列表尾部追加。该方式打印杨辉三角所有元素
m = 5
k = 4
a = []
for i in range(m):
    newline = [1]
    a.append(newline)
    if i == 0: continue
    for j in range(i-1):
        newline.append(a[i-1][j] + a[i-1][j+1])
    newline.append(1)
print(a)
print(a[m-1][k-1])
# 方法二：不断的产生新旧两个列表。优于方法一，当大数据时，产生大列表效率比较低
m = 6
k = 3
oldline = [1, 1]
for i in range(2, m):
    newline = [1]
    for j in range(i-1):
        newline.append(oldline[j] + oldline[j+1])
    newline.append(1)
    oldline = newline
if m < 2:
    for k in range(2):
        oldline = [1] * k
print(oldline)
print(oldline[k-1])
# 方法三：一次性开辟指定长度列表（新旧列表交替使用）
m = 6
k = 5
oldline = []
for i in range(m):
    newline = [1] * (i + 1)     # 一次性开辟所要的空间（相比append效率稍好）
    for j in range(i-1):
        newline[j+1] = oldline[j] + oldline[j+1]
    oldline = newline
print(newline)
# 方法四：杨辉三角公式算法
m = 6
k = 4
n = m - 1   # 默认是从0开始，通常说的第几项是从1开始，所以需要-1
r = k - 1
d = m - k
factorial = 1
targets = []     # r! d! n!   公式：n!/(r!*d!)
for i in range(1, n+1):
    factorial *= i
    if r == i:
        targets.append(factorial)
    if d == i:
        targets.append(factorial)
    if n == i:
        targets.append(factorial)
print('{}'.format(targets[2] // (targets[0] * targets[1])))
'''
# 给定一个3*3的方阵，求其转置矩阵
'''
a = [[1, 2, 3],     # [1, 4, 7]
     [4, 5, 6],     # [2, 5, 8]
     [7, 8, 9]]     # [3, 6, 9]
for i in range(len(a)):
    for j in range(i):  # 隐含条件j<i
        a[i][j], a[j][i] = a[j][i], a[i][j]
print(a)
'''
# 给定一个矩阵，求其转置矩阵
'''
# 方法一：随时创建，append追加
lst = [[1, 2, 3],     # [1, 4]
     [4, 5, 6]]     # [2, 5]
                    # [3, 6]
result = []
for a in lst:  # a=[1,2,3]  [4,5,6]
     for i, value in enumerate(a):      # i=0 1 2 0
          if len(result) < i+1:         #
               result.append([])        # result=[[]] [[],[]] [[],[],[]]
          result[i].append(value)       # [[1]] [[1],[2]] [[1],[2],[3]] [[1,4],[2],[3]]
print(result)
# 方法二：一次性开辟空间
lst = [[1, 2, 3],     # [1, 4]
       [4, 5, 6]]     # [2, 5]
                      # [3, 6]
a = [[0 for i in range(len(lst))] for j in range(len(lst[0]))]
for i, b in enumerate(lst):             # i=[1,2,3]
     for j, value in enumerate(b):      # j=0 v=1 ; j=1 v=2
          a[j][i] = value               # a00=1; a11=2; a=33=3
print(a)
# 高效方法
lst = [[1, 2, 3], [4, 5, 6]]
a = [[0 for i in range(len(lst))] for j in range(len(lst[0]))]
for i in range(len(a)):
     for j in range(len(a[0])):
          a[i][j] = lst[j][i]
print(a)
'''
# 随机产生10个数字，要求：数字取值范围[1,20],统计重复数字有几个？分别是什么？不重复数字有几个，分别是什么？
'''
import random
a = [random.randrange(10) for _ in range(10)]
c = 0
b = [0 for i in range(len(a))]
repeat = []
diff = []
for i in range(len(a)):
     if b[i] != 0:continue
     cout = 0
     for j in range(i+1, len(a)):
          if b[i] != 0: continue
          c += 1
          if a[i] == a[j]:
               cout += 1
               b[j] = cout
     if cout:
          b[i] = cout + 1
          repeat.append([a[i], b[i]])
     else:
          diff.append(a[i])
print(a)
print(b)
print('repeat number is :{}'.format(repeat))
print('not repeat number is :{}'.format(diff))
print(c)
'''
# 取2组10个随机数，范围[10,20]
'''
# 判断这2组数一共有多少个不重复的数
# 比较这2组数，有多少个不重复的数，分别是多少
# 比较这2组数，有多少个重复的数，分别是多少
import random
a = [15, 14, 14, 10, 17, 16, 17, 13, 14, 17]
b = [16, 16, 13, 18, 20, 15, 19, 13, 13, 16]
for i in range(10):
     a.append(random.randrange(10, 21))
     b.append(random.randrange(10, 21))
a1 = set(a)
b1 = set(b)
print(a1)
print(b1)
print(a1 | b1)
print(len(a1 ^ b1), a1^b1)  # 切记，如果用-，则会少了b1的不重复数
print(len(a1 & b1), a1&b1)
'''
# 拿到一个数，统计每位数重复出现的次数  **************字典
'''
n = ' 054325543210 '.strip(' ').lstrip('0')
d = {}
for i in n:
     d[i] = d.get(i, 0) + 1      # get功能，定义缺省为0，当i不在d内时，返回0并+1，则第一次计数为1；当i在d内时，get返回i的value，再加1，从而达到计数目的
     # d[i] = d.setdefault(i, 0) + 1      # setdefault功能与get功能类似
print(d)
'''
# 数字统计
'''
# 1.随机产生100个数字。2.数字范围【-1000， 1000】。3.升序输出这些数字并打印其重复的次数
import random
nums = [random.randint(-1000, 1000) for _ in range(100)]   # 列表解析式
count = {}
for i in nums:
    count[i] = count.get(i, 0) + 1
newlist = sorted(count.items())
print(newlist)
'''
# 从26个小写字符串中，随机取两个字符，共取100个。统计每个字符重复出现的次数，并升序打印
'''
import random
# for i in range(26):
#      strs += chr(97 + i)  # 产生26个小写英文字母
strs = 'abcdefghijklmnopqrstuvwxyz'
strlist = [random.choice(strs) + random.choice(strs) for _ in range(100)]
# for i in range(100):
#      strlist.append(random.choice(strs) + random.choice(strs)) # 等同上面列表内的解析式
strdict = {}
for i in strlist:
     strdict[i] = strdict.get(i, 0) + 1

print(sorted(strdict.items(), reverse=True))
'''
# 列表解析式练习
'''
# 一个列表的元素是【1,10】的每一个数的平方
a = [i**2 for i in range(1, 11)]
# 产生一个新列表，其元素是lst列表中相邻元素的和
lst = [1, 4, 9, 16, 2, 5, 10, 15]
newl = [lst[i]+lst[i+1] for i in range(len(lst)-1)]
#  打印99乘法表
b = [print('{}*{}={:<{}}'.format(y, x, x*y, 2 if y == 1 else 3), end='\n' if x == y else '') for x in range(1, 10) for y in range(1, x+1)]
# 产生100个ID，要求以点分割，前面带4位升序序号，后面跟10个小数字母，例如：“0001.aeakskoed"
import string
import random
c = ['{:04}.{}'.format(i, ''.join(random.choices(string.ascii_lowercase, k=10))) for i in range(1, 101)]
print(c)
'''
# 简单选择排序
'''
a = [4, 7, 5, 6, 0, 9, 2, 1, 3, 8]
length = len(a)
for i in range(length-1):
    maxindex = i
    for j in range(i+1, length):
        if a[j] > a[maxindex]:
            maxindex = j
    if maxindex != i:   # 当最大数的index与i相同时，即表示不需要进行交换
        a[i], a[maxindex] = a[maxindex], a[i]
print(a)
'''
# 简单选择排序升级===找最大值得同时，也找最小值，一个正索引查找，一个负索引查找
'''
import random
a = [4, 7, 5, 6, 0, 9, 2, 1, 3, 8]
random.shuffle(a)
print(a)
length = len(a)
for i in range(length//2):  #  迭代数值减半
    maxindex = i
    minindex = -i-1
    for j in range(i+1, length-i):  # 尾部区间为length-i====j的取值为列表的正负两段不断减少
        if a[j] > a[maxindex]:
            maxindex = j
        if a[-j-1] < a[minindex]:
            minindex = -j-1
    if a[maxindex] == a[minindex]:      # 当某趟后发现，最大值和最小值相等，则表示剩余数字相等
        break
    if maxindex != i:
        a[i], a[maxindex] = a[maxindex], a[i]
        if minindex == i - length:   # 当找最大值时，出现当前交换的是最小值时，增加判断
            minindex = maxindex - length
    if minindex != -i-1:
        a[-i-1], a[minindex] = a[minindex], a[-i-1]
print(a)
'''
# 从下面链接中找出 .gz 结尾的链接，并将符合要求链接的文件名按顺序输出。（提示：最终要的是.gz结尾的包名，例如coreutils-6.11.tar.gz ）
'''
urls = '
# mirrors.kernel.org/gnu/coreutils/coreutils-6.11.tar.gz 
# mirrors.kernel.org/gnu/bash/bash-5.0.tar.gz
# www.baidu.com/ 
# www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.1.2/hadoop-3.1.2-src.tar.gz 
# apache.org/dist/hbase/2.1.4/api_compare_2.1.3_to_2.1.4RC1.html
# www.apache.org/dyn/closer.lua/hbase/2.1.4/hbase-2.1.4-src.tar.gz
# tomcat.apache.org/download-90.cgi 
# mirrors.kernel.org/gnu/grub/grub-2.02.tar.xz 
# mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-9/v9.0.19/bin/apache-tomcat-9.0.19-fulldocs.tar.gz 
# archive.apache.org/dist/zookeeper/current/zookeeper-3.4.14.tar.gz 
# hub.docker.com/editions/community/docker-ce-desktop-mac 
# home.firefoxchina.cn/ 
# docs.ceph.com/docs/master/'

urlList = urls.split()  # 对字符串用空格分割====产生列表，并能去除空格
filelist = []
for url in urlList:
    if url.endswith('.gz') and url.startswith('www'):   # 判断列表每项以www开头和以。gz结尾
        filelist.append(url.split('/')[-1])     # 再以/分割，产生列表，取列表最后一项，并append到新列表中
print(sorted(filelist))     # 对新列表进行sort排序
'''
# 输入一个数字，打印相应的图形======计算最长一行的思想，避免重复计算
'''
# 思路一，计算出最长的一行，然后依次从该行中取数
n = 12
charlist = [str(i) for i in range(1, n+1)]
strlength = len(' '.join(charlist))
print(charlist)
for i in range(1, n+1):
    print('{:>{}}'.format(' '.join([charlist[i] for i in range(i-1, -1, -1)]), strlength))
    # print(' '.join([charlist[i] for i in range(i)]))

# 切片思想
n = 12
tail = [str(i) for i in range(1, n+1)]
for i in range(1, n+1):
    print(' '.join(tail[:i]))

n = 12
tail = [str(i) for i in range(n, 0, -1)]
strlength = len(' '.join(tail))
for i in range(n):
    print('{:>{}}'.format(' '.join(tail[i:]), strlength))
print(tail)
'''




