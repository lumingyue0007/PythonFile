

# 方法一，数字处理方式
def base64_decode(src:bytes):
    alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    alp_dict = dict(zip(alphabet, range(64)))
    target = bytearray()
    # 判断输入字串是否是4的倍数，否则警报
    length = len(src)
    if length % 4:
        print('input error')
        return
    # 每次从字串中取出4个为一组
    for i in range(0, length, 4):
        _src = src[i:i+4]
        # 从每组字串中，依次迭代每个字符，并查表，返回index --->由于find查找需要变量，效率不高，所以改为字典，用索引访问
        val = 0
        for i, char in enumerate(_src):
            index = alp_dict.get(char)
            # 如果没有找到，返回None，则特殊处理
            if index is not None:
                # 索引左移相加
                val += index << (3-i)*6
        # 数字转换为bytes，每三个为一组，尾部去除\x00，由于生成的是bytes，所以要用extend迭代到bytearry
        target.extend(val.to_bytes(3, 'big').strip(b'\x00'))
    return bytes(target)

print(base64_decode(b'YmR4YWVhc2VxcQ==')) # bdxaeaseqq

# 方法二，字符串处理方式
def base64_dcoder(src:bytes):
    alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    alp_dict = dict(zip(alphabet, range(64)))
    # 判断输入字串是否是四的整数倍，否则报错
    length = len(src)
    if length % 4:
        print('input error')
        return
    else:
        # 四组一取
        target = bytearray()
        for i in range(0, length, 4):
            mix_str = ''
            for i in src[i:i+4]:
                if i != 61:
                    # index = alphabet.find(i)  # 由于find是遍历，效率不好，改为下面的字典，直接get，索引访问
                    index = alp_dict.get(i)
                    # 拼接二进制字串 4*6
                    mix_str += '{:0>6}'.format(str(bin(index)).replace('0b', ''))
                else:
                    mix_str += '0' * 6
            target.extend(int(mix_str, 2).to_bytes(3, 'big').rstrip(b'\x00'))
        # # 4*6 --> 3*8
        # for i in range(0, len(mix_str), 8):
        #     ret += chr(int(mix_str[i:i+8], 2))

        return bytes(target)

