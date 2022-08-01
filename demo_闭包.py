#闭包的形成，内部函数要使用外部函数的变量,返回内部函数
def func1(name):
    def func2(msg):
        print(name + ':'+ msg)

    #返回内部函数
    return func2

tom = func1('tom')
tom('开始出发')

#装饰器，不改变原函数，对原函数额外添加新的功能
#定义装饰器
def func3(func):
    def inner():
        #在内部函数对函数进行装饰
        print('登录校验')
        func()
    return inner
def func5(func):
    def inner():
        print('登录中。。。')
        func()
    return inner

@func3 #语法糖写法装饰函数 先执行
@func5 #后执行
def func4():
    print('发表评论')
func4()