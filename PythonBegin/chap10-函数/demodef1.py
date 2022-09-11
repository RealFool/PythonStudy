# 李亚钦
# 2022/7/22 22:43
def fun(num):
    odd = []    # 奇数
    even = []   # 偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


print(fun([10, 25, 12, 36, 55, 11, 30]))
