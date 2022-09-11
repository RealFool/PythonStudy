# 李亚钦
# 2022/7/23 23:41
""""with上下文管理器，无论何时跳出with确保文件自动关闭，释放资源，无需手动用户关闭"""
with open('a.txt', 'r', encoding='UTF-8') as file:
    print(file.read())


"""如何实现上下文管理器：重写__enter__与__exit__方法"""
class MyContentMgr(object):
    def __enter__(self):
        print('enter执行')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit执行')

    def show(self):
        print('show', self)


with MyContentMgr() as mgr:     # 相当于mgr = MyContentMgr()
    mgr.show()
