# a = 1
# while a < 10:
#     print(a)
#     a+=1

#0-4的累加
# a = 0
# sum = 0
# while a < 5:
#     sum += a
#     a += 1
#     print(sum)

#1-100的偶数和2550
# b = 1
# sum = 0
# print(b%2)
# while b <= 100:
#     print(b)
#     if not bool(b%2):
#         sum += b
#     else:
#         pass
#     b+=1
#     print(sum)

# for item in 'python':
#     print(item)

#循环体不需要用到变量可使用_为自定义变量
# for _ in range(10):
#     print('辣鸡python')

#1-100的偶数和
# sum = 0
# for item in range(1,101):
#     if not bool(item % 2):
#         sum += item
#
# print(sum)

#100-999的水仙花数和
# sum = 0
# for item in range(100,1000):
#     g = item % 10
#     s = item // 10 % 10
#     b = item // 100
#     if g**3 + s**3 + b**3 == item:
#         print(item)
#         sum += item
# print(sum)

#break退出循环体
# for item in range(3):
#     psw = input('请输入密码：')
#     if psw == '888888':
#         print('密码正确')
#         break
#     else:
#         print('密码输入错误')

#continue 结束当前循环继续下一次循环
# for item in range(3):
#     if item == 1:
#         continue
#     print(item)

#else
# for item in range(3):
#     psw = input('请输入密码：')
#     if psw == '888888':
#         print('密码输入正确')
#         break
#     else:
#         print('密码输入错误')
# else:
#     print('三次密码输入错误')

#矩形
# for i in range(3):
#     for j in  range(4):
#         print('*',end='\t')
#     print()

#乘法表
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(str(i) + '*' + str(j) + '=' + str(i*j),end='\t')
#     print()