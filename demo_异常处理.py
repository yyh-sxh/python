#异常处理完整结构
# try:
#     a = int(input('请输入一个整数：'))
#     b = int(input('请输入另一个整数：'))
#     sum = a / b
# except BaseException as e:
#     print('出错了',e)
# else:
#     print(sum)
# finally:
#     print('程序结束')

#常见的异常类型
#ZeroDivisionError 除（或取模）零（所有数据类型）
#indexError 序列中没有此索引
#KeyError 映射中没有这个键
#NameError 未声明/初始化对象（没有属性）
#SyntaxError Python语法错误
#ValueError 传入无效的参数

#traceback的使用
import traceback
# try:
#     print('----------------')
#     print(1/0)
# except:
#     traceback.print_exc()

i = 1
while i <= 5:
    print(i)
    i+=1