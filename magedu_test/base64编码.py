
# base64编码
# 方法一
def base64_encoder(src:str):
    alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    target = bytearray()
    # 将字符串转换为bytes，防止不同编码规则下，占有不同字节长度，比如中文
    if isinstance(src, str):
        _src = src.encode()
    else:
        print('error')
        return
    # 从目标中每次取出3个字符，如果不足3个，则用asic码空补全
    length = len(_src)
    r = 0
    for offset in range(0, length, 3):
        tipe = _src[offset:offset + 3]
        if len(tipe) < 3:
            r = 3 - len(tipe)
            tipe += b'\x00' * r
        # 3*8转换为4*6
        val = int.from_bytes(tipe, 'big')  # bytes ==> int
        for i in range(18, -1, -6):
            index = val >> i & 0x3F
            target.append(alphabet[index])
    # 替换
    # for i in range(1, r+1):
    #     target[-i] = 61
    if r:
        target[-r:] = b'=' * r   # bytearray从-r到尾部用‘=’填充
    return bytes(target)

print(base64_encoder('你好'))
import base64
print(base64.b64encode('你好'.encode()))


# 方法二
def base_encode(string:str)->str:
    oldstr = ''
    newstr = []
    base = ''
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
    #把原始字符串转换为二进制，用bin转换后是0b开头的，所以把b替换了，首位补0补齐8位
    for i in string:
        oldstr += '{:08}'.format(int(str(bin(ord(i))).replace('0b', '')))
    #把转换好的二进制按照6位一组分好，最后一组不足6位的后面补0
    for j in range(0, len(oldstr), 6):
        newstr.append(oldstr[j:j + 6])
    #在base_list中找到对应的字符，拼接
    for l in range(len(newstr)):
        if len(newstr[l]) < 6:
            # newstr[l] = '{:0<6}'.format(newstr[l])
            newstr[l] += '0' * (6 - len(newstr[l]))
        base += base64_list[int(newstr[l], 2)]
    #判断base字符结尾补几个‘=’
    if len(string) % 3 == 1:
        base += '=='
    elif len(string) % 3 == 2:
        base += '='
    return  base

print(base_encode('你好'))








