
# 求两个字串的最长公共子串
# 方法一，矩阵算法
s1 = 'abcdefghijklmn'
s2 = 'defabcdfjijklmn'

def fx(str1:str, str2:str):
    # 判断str1和str2的长度，并确定str1为最短字串
    length1 = len(str1)
    length2 = len(str2)
    if length1 > length2:
        str1, str2 = str2, str1
    # 从最小的字串中选择字串与最大的字串进行比较，并做标记
    matrix = [[0] * length1 for i in range(length2)]    # 创建矩阵
    xmax = 0
    xindex = 0
    for i, x in enumerate(str2):
        for j, y in enumerate(str1):
            if x == y:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                if xmax < matrix[i][j]:
                    xmax = matrix[i][j]
                    xindex = j
    start = xindex + 1 - xmax
    end = xindex + 1
    return str1[start:end]

print(fx(s1, s2))

# 方法二：字符串截取，效率不高
def fn(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 > length2:
        str1, str2 = str2, str1

    for sublen in range(length1, 0, -1):
        for start in range(0, length1 - sublen + 1):
            substr = str1[start:start + sublen]
            if str2.find(substr) > -1:
                return substr

print(fn(s1, s2))

# 方法三
def fy(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 > length2:
        str1, str2 = str2, str1

    def _fn(_str1, _str2, start=0, end=1, max_str=''):
        if end > length1:
            return max_str
        else:
            if _str1[start:end] in _str2:
                if len(_str1[start:end]) > len(max_str):
                    max_str = _str1[start:end]
                end += 1
            else:
                start += 1
                end = start + 1
            return _fn(str1, str2, start=start, end=end, max_str=max_str)
    return _fn(str1, str2)

print(fy(s1, s2))