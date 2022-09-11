# 李亚钦
# 2022/7/22 22:53
# 个数可变的位置参数
def fun(*args):
    print(args)


fun(10)
fun(10, 20, 30)


# 个数可变的关键字形参
def fun2(**args):
    print(args)


fun2(a=10)
fun2(a=10, b=20)


# 函数调用传参
def fun3(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun3(10, 20, 30)  # 位置传参
lst = [1, 2, 3]
fun3(*lst)  # 转化为位置传参
print('------------------')
fun3(a=10, b=20, c=30)  # 关键字传参
dic = {'a': 1, 'b': 2, 'c': 3}
fun3(**dic)  # 转化为位置传参


# 位置形参和关键字形参混合
def fun4(a, b, *, c, d):    # 从*之后的参数必须采用关键字传参，否则报错
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


print('-----------------------------')
fun4(10, 20, c=30, d=40)
