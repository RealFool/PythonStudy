# 李亚钦
# 2022/7/23 22:14
def add(a, b):
    return a + b


"""只有calc是主程序的时候（点击运行calc的时候）才会运行这里的内容，外部导入将不会调用这里"""
if __name__ == '__main__':
    print(add(10, 20))
