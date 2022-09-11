# 李亚钦
# 2022/7/21 23:33
# 创建list的两种方式
# 一、[]
lst = ['hello', 'world', 10, 'hello']

# 二、内置函数list()
lst2 = list(['hello', 'world', 10])

# 简单操作
print(lst)
print(lst[0], lst[-3])
print(lst.index('hello'))
print(lst.index('hello', 1, 4))

# 切片 list[start:stop:step]， start默认为0，stop默认最后，step默认为1
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst)
print(id(lst), id(lst[1:3:1]))
print(lst[1:3:1])
print(lst[:3:])
print(lst[1::1])

# 切片步长可为负数，从后往前
print('--切片步长负数--')
print(lst[::-1])  # step=-1表示从后往前
print(lst[7::-1])
print(lst[::-2])
