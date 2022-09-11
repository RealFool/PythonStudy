# 李亚钦
# 2022/7/21 18:58
# range()函数的使用
# 方式一
r = range(10)  # 从0开始，到10结束，步长1
print(r)
print(list(r))

# 方式二
r = range(1, 10)  # 从1开始，到10结束，步长1
print(list(r))

# 方式三
r = range(1, 10, 2)  # 从1开始，到10结束，步长2
print(list(r))

# in 与 not in 的使用
print(9 in r)
print(10 in r)
