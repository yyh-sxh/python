class A(object):
    pass

class B(object):
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

x = C('jack',20)
print(x.__dict__)