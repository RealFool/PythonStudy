# 李亚钦
# 2022/7/21 11:25

# sex = input("性别：")
# print(sex)

# 整除
print(11 // 5)
# 幂运算
print(2 ** 2)

# 同号向上取整，异号向下取整
print(9 // 4)
print(-9 // -4)
print(-9 // 4)
print(9 // -4)

# 取余，异号按照公式
print(-9 % 4)  # 余数=被除数-除数*商  -9-(4*(-3)) = -9+12 = 3

# 链式赋值
a = b = c = 10
print(a, id(a))
print(b, id(b))
print(b, id(b))

# 解包赋值
a, b, c = 10, 20, 30
print(a, b, c)

# 交换值
a = 10
b = 20
print('交换前：', a, b)
a, b = b, a
print('交换后：', a, b)

# 比较
x = 10
y = 10
print(x == y)  # 比较值
print(x is y)  # 比较标识
print(x is not y)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)

# 布尔运算符 and, or, not, in, not in
print('布尔运算符')
a = 1
b = 2
print(a == 1 and b == 2)
print(a == 1 or b != 2)
bo = True
print(not bo)
s = 'hello'
print('e' in s)
print('e' not in s)

print(1 in list1)

# 位运算符，二进制比较
print('位运算符')
print(4 & 8)  # 按位与，对应位同为1是1，其他情况为0
print(4 | 8)  # 按位或，对应为同为0是0，其他情况为1

# 移位运算符
# 右移一位，相当除2，20100 -> 0010 2
print(4 >> 1)
# 左移一位，相当乘2，0100 -> 1000 8
print(4 << 1)

# 运算符优先级：算数运算 > 位运算 > 比较运算 > 布尔运算 > 赋值运算
