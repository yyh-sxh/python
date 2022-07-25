#类的创建,类名由一个或多个单词组成，每个单词首字母大写，其余小写
class Student:
    native_pace = '吉林' #直接写在类里面的变量，称为类属性

    #初始化方法
    def __init__(self,name,age):
        self.name = name #self.name 称为实体属性
        self.age = age

    #实例方法
    def eat(self):
        print('学生在吃饭...')

    #静态方法
    @staticmethod
    def method():
        print('我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法')

#对象创建
stu = Student('张三',20)
# print(stu.name)
# print(stu.age)
# stu.eat()
# Student.method()
# Student.cm()

#动态绑定属性
stu.gander = '男'

#动态绑定方法
def show():
    print('定义在类外面的方法')
stu.show = show
stu.show()