# 使用二分法，在序列中插入相应的数
src = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51, 100]
# 二分法，序列必须为已排序序列
src = sorted(src)

def insert_sort(orderlist, i):
    ret = orderlist[:]  # 复制一份
    low = 0
    high = len(orderlist)
    while low < high:
        mid = (low + high) // 2
        if orderlist[mid] < i:
            low = mid + 1
        else:
            high = mid
    ret.insert(low, i)
    return ret

# r = src
# for x in (40, 60, 100):
#     r = insert_sort(r, x)
#     print(r)

import bisect # 二分法

def get_grade(score:int):
    src_list = [60, 70, 80, 90]
    grades = 'EDCBA'
    return grades[bisect.bisect(src_list, 85)]

print(get_grade(80))




