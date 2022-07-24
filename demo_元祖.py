#元祖的创建,单个元祖时需要再后面加逗号
# a = ('python','hello',98)
# b = ('python',)
# c = 'python',
# print(type(b))
# print(type(c))
#
# d = tuple(('python','hello'))
# print(d)
# print(type(d))

#元祖不支持增删改
t = (10,[20,30],{'name':'张三'})
# print(t[0])
# print(t[1])
# t[0] = 44 #报错
# print(t)

#元祖中的对象或数组可进行增删改
# t[1].append(50)
# print(t)
# t[2]['name']='李四'
# print(t)

#元祖的遍历
# for item in t:
#     print(item)

