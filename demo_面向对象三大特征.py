#封装
class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age #不希望在类的外部使用，在前面加__
    def start(self):
        print('开始跑路...')
stu = Student('张三',20)
# stu.start()
# print(stu._Student__age) #在类的外部访问age，不建议使用

#继承,一个类如果没有继承任何类，则默认继承object
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student1(Person):
    def __init__(self,name,age,no):
        super().__init__(name,age)
        self.no = no

class Teacher(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year = year

stu1 = Student1('张三',18,131)
teacher = Teacher('李四',30,5)
# stu1.info()
# teacher.info()

#多继承,C类同时继承A类和B类
class A:
    pass
class B:
    pass
class C(A,B):
    pass