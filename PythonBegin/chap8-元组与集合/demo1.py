# 李亚钦
# 2022/7/22 14:49

"""元组的创建"""
"""方式一，()"""
tup = ('hello', 10, True)
print(tup, type(tup))
tup0 = 'hello', 'world', 10  # ()可省略
print(tup0, type(tup0))
tup1 = ('hello',)  # 当只有一个元素的时候，元组要以,结尾
print(tup1, type(tup1))

"""方式二，内置函数tuple()"""
tup2 = tuple(('world', 20, False))
print(tup2, type(tup2))


"""遍历元祖"""
for i in tup:
    print(i)
