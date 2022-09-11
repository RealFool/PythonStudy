# 李亚钦
# 2022/7/23 19:06
class Student:
    native_pace = '河南'  # 类变量

    def __init__(self, name, age, sno):
        self._Student__sno = None  # 想访问__sno时，通过这个访问
        self.name = name
        self.age = age
        self.__sno = sno    # 不希望该属性在外部被使用，在名字前面加__，当然想使用也有其他方式

    # 实例方法  类外面的是函数，类里面的为方法
    def eat(self):
        print(self.name, '在吃饭')

    # 静态方法  使用类名直接访问
    @staticmethod
    def method():
        print('使用staticmethod修饰，静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('使用classmethod修饰，类方法')

    @property
    def Student__sno(self):
        return self._Student__sno


# 创建Student对象
stu = Student('Zhangsan', 20, '111')
stu.eat()
print(stu.name)
print(stu.age)
stu.cm()
stu.method()
print('-------------------------使用__定义的属性----')
print(dir(stu))
print(stu.Student__sno)

print("------------------------------------")
Student.eat(stu)  # 与stu.eat()作用相同， 但需要传过去一个Student对象，self
Student.cm()  # 而类方法和静态方法可以直接用类名访问
Student.method()

print('---------------------------------')
stu1 = Student('Zhangsan', 20, '222')
stu2 = Student('Lisi', 22, '333')
print('------------------------为stu1动态绑定性别属性-----------------')
stu1.gender = '女'
print(stu1.name, stu1.age, stu1.gender)
print(stu2.name, stu2.age)

print('------------------------为stu1动态绑定方法--------')


def show():
    print('show show way')


stu1.show = show
stu1.show()
