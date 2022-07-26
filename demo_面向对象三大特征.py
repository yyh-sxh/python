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

    def __str__(self): #重写返回描述
        return f'我的名字是{self.name},今年{self.age}岁'

    def info(self):
        print(self.name,self.age)

class Student1(Person):
    def __init__(self,name,age,no):
        super().__init__(name,age)
        self.no = no

    def info(self): #方法重写
        super().info() #调用父类方法
        print(self.no)


class Teacher(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year = year
    def info(self): #方法重写
        super().info()
        print('教龄:' + str(self.year))

stu1 = Student1('张三',18,131)
teacher = Teacher('李四',30,5)
stu1.info()
teacher.info()
print(stu1)

#多继承,C类同时继承A类和B类
class A:
    pass
class B:
    pass
class C(A,B):
    pass

#多态
class Animal:
    def eat(self):
        print('动物会吃')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Per:
    def eat(self):
        print('人吃五谷杂粮')

def fun(obj):
    obj.eat()

fun(Cat()) #猫吃鱼
fun(Dog()) #狗吃骨头
fun(Animal()) #动物会吃
fun(Per()) #人吃五谷杂粮