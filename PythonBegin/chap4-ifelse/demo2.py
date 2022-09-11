# 李亚钦
# 2022/7/21 18:30
# 银行取款
money = 1000
qu = int(input('请输入取款金额：'))
if money > qu:
    money -= qu
    print('取款成功，余额：', money)
elif money == qu:
    print('取完了')
else:
    print('余额不足')
