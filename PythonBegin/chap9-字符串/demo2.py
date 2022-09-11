# 李亚钦
# 2022/7/22 20:05
"""字符串常用操作"""
s1 = 'Hello, python'
print(s1)
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())

"""字符串对齐"""
"""居中对齐"""
print(s1.center(20, '*'))
print(s1.center(20))
print(s1.center(10))
"""左对齐"""
print(s1.ljust(20, '*'))
print(s1.ljust(20))
print(s1.ljust(10))
"""右对齐"""
print(s1.rjust(20, '*'))
print(s1.rjust(20))
print(s1.rjust(10))
"""右对齐，0填充"""
print(s1.zfill(20))
print('--1111'.zfill(9))

"""字符串分割"""
s2 = 'hello world python'
s3 = 'hello|world|python'
print(s2.split())   # 默认分隔符是空格
print(s3.split(sep='|'))    # 指定分隔符
print(s3.split(sep='|', maxsplit=1))    # 指定最大分割次数
print('------rsplit------')
print(s3.rsplit(sep='|', maxsplit=1))

"""判断字符串操作"""
print('1.', 'hello,world'.isidentifier())     # 判断是否是标识符（字母，数字，下划线，组成）
print('2.', '张三_'.isidentifier())

print('3.', ''.isspace())   # 空白字符
print('4.', '\t'.isspace())
print('5.', ' '.isspace())

print('6.', 'hello'.isalpha())    # 字母
print('8.', '张三'.isalpha())
print('8.', 'aa,'.isalpha())

print('9.', '10'.isdecimal())  # 十进制
print('10.', '一二三'.isdecimal())
print('11.', 'ⅠⅡⅢⅣ'.isdecimal())

print('12.', '100'.isnumeric())  # 数字
print('13.', '一二三'.isnumeric())
print('15.', 'ⅠⅡⅢⅣ'.isnumeric())

print('16.', 'hello666'.isalnum())  # 字母和数字
print('17.', '一二三hh'.isalnum())
print('18.', '张三123'.isalnum())
print('19.', 'aaaⅠⅡⅢⅣ'.isalnum())

"""字符串替换"""
print('-----------replace------------')
s4 = 'hello python python python'
print(s4.replace('python', 'java'))
print(s4.replace('python', 'java', 2))  # 可指定最大替换数量

print('-------------join--------------')
lst = ['hello', 'python', 'world']
print(lst)
print('|'.join(lst))
print('*'.join(lst))
print(''.join(lst))

tup = ('hello', 'tuple', 'python')
print(tup)
print('*'.join(tup))
print(''.join(tup))

s = 'hellopython'
print('*'.join(s))

"""字符串切片"""
print('-----------------字符串切片[start:stop:step]--------------------')
s5 = 'Hello,Python'
print(s5[:5])
print(s5[6:])

"""字符串格式化"""
print('--------------------------占位符----------------------------')
"""一、%占位符"""
name = '张三'
age = 20
print('我叫%s，几年%d岁了' % (name, age))
"""二、{}"""
print('我叫{0}，今年{1}岁了，我真的叫{0}'.format(name, age))
"""三、f-string"""
print(f'我叫{name}，几年{age}岁了')

"""字符串编码和解码"""
print('------------------------字符串编码和解码----------------------------')
s6 = '床前明月光'
print(s6.encode(encoding='GBK'))  # GBK，一个中文两个字节
print(s6.encode(encoding='UTF-8'))   # UTF-8，一个中文三个字节

byte = s6.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
