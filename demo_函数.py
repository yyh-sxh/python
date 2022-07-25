def cale(a,b):
    c = a + b
    return c
#位置实参
sum = cale(10,20)
# print(sum)

#关键字实参
result = cale(b=10,a=20)
# print(result)

#函数内改变实参，不可变对象无法修改实参，可变对象可以改变实参
def fun(arg1,arg2):
    arg1 = 100
    arg2.append(10)
    return
n1 = 11
n2 = [20,30]
fun(n1,n2)
# print(n1) #11
# print(n2) #[20,30,10]

#retrun返回值,没有返回值return可不写，只有一个直接返回类型，多个返回值结果为元祖
def fun2():
    # print('hello')
    return
fun2()

def fun3():
    return 'hello'
result = fun3()
# print(result)

def fun4():
    return 'hello','world'
result = fun4()
# print(result)

#函数默认值参数
def fun5(a,b=10):
    return  a + b
sum1 = fun5(100)
# print(sum1)
sum2 = fun5(100,40)
# print(sum2)

#函数参数个数未知,函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，位置形参要放在关键字形参前面，位置参数只能有一个
#可变位置参数,返回元祖
def fun6(*args):
    print(args)
# fun6(10)
# fun6(10,20)

#可变关键字参数,返回json对象
def fun7(**args):
    print(args)
# fun7(a=10)
# fun7(a=10,b=20)

#函数内声明全局变量
def fun8():
    global myname
    myname = '张三'
fun8()
# print(myname) #张三

#递归函数
def fun9(n):
    if n == 1:
        return n
    else:
        return n*fun9(n-1)
sum = fun9(6)
# print(sum)