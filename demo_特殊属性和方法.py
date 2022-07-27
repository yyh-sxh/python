class A(object):
    pass

class B(object):
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

x = C('jack',20)
# print(x.__dict__)

class Student(object):
    def __init__(self,name):
        self.name = name

    def __add__(self, other):  #实现两个对象的加法，重写__add__方法
        return  self.name + other.name

    def __len__(self):         #重写len方法返回的内容长度
        return len(self.name)

stu1 = Student('张三')
stu2 = Student('李四')
s = stu1 + stu2 #实现两个对象的加法，重写__add__方法
print(s)
print(len(stu1))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs): #生成新的对象，return到self中
        obj = super().__new__(cls)
        return  obj

p1 = Person('张三',20)

#浅拷贝，只拷贝原对象，子对象不拷贝
class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

cpu1 = CPU()
disk = Disk()
computer1 = Computer(cpu1,disk)

import copy #引入模块包
computer2 = copy.copy(computer1)
print(computer2,computer2.cpu,computer2.disk)
print(computer1,computer1.cpu,computer1.disk)

#深拷贝,原对象、子对象都拷贝
computer3 = copy.deepcopy(computer1)
print(computer3,computer3.cpu,computer3.disk)