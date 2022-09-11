# 李亚钦
# 2022/7/23 20:22

# 父类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


# Student子类
class Student(Person):
    def __init__(self, name, age, sno):
        super().__init__(name, age)
        self.sno = sno

    # 方法重写
    def info(self):
        super().info()
        print(self.sno)


# Teacher子类
class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age, )
        self.teachofyear = teachofyear

    # 方法重写
    def info(self):
        super().info()
        print(self.teachofyear)


stu = Student('张三', 20, '1001')
tea = Teacher('李四', 34, 10)
stu.info()
tea.info()
