# 李亚钦
# 2022/7/21 22:58
"""
    for...else... ; while...else...
    若循环中没有执行break，则执行else
"""

for i in range(3):
    pwd = input("请输入密码：")
    if pwd == '666':
        print("密码正确！")
        break
    else:
        print("密码错误，请重试！")
else:
    print("对不起，三次密码均输入错误！")
