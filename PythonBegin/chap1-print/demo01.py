# 李亚钦
# 2022/7/20 23:34

# 转义字符
print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\tworld')  # 回车覆盖
print('hello\bworld')  # 退一位

# 不希望转义字符起作用, r或R，最后一个字符不能使\
print(r'hello\nworld')
