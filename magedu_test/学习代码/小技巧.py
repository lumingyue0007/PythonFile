
# 查找list中出现次数最多的元素，并显示该元素出现的次数

a = [1,2,3,4,2,3,1,2,1,2,2]
print(max(set(a),key=a.count))

from collections import Counter
cnt = Counter(a)
print(cnt.most_common(1))



