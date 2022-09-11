# 李亚钦
# 2022/7/23 0:05
"""程序抛出异常，执行except，没有异常才会执行else，finally块无论是否发生异常都会执行（通常用来释放资源）"""
try:
    a = input('请输入一个被除数：')
    b = input('请输入一个除数：')
    result = int(a)/int(b)
    print('结果为：', result)
except ValueError:
    print('只能输入数字')
except BaseException as e:
    print("出错了：", e)
else:
    print("程序结束")
finally:
    print("资源释放，谢谢使用")

