# list = ['hello','world',98,'hello']
# print(list.index('hello'))
# print(list.index('hello',1))
# print(list[0])
#

# lst = [10,20,30,40,50,60,70,80]
#数组切片，会产生新数组
#start = 1,end = 6, step默认
# print(lst[1:6])
#start = 1,end = 6, step =
# print(lst[1:6:2])
#start = 1,end默认, step默认
# print(lst[1:])
#start默认,end = 6, step默认
# print(lst[:6])
#start默认,end默认，step = -1,步长为负数逆序
# print(lst[5::-1])

#判断对象是否存在数组中
# print(10 in lst) #true
# print(55 in lst) #false

#数组遍历
# for item in lst:
#     print(item)

#数组追加单个元素
# lst.append(90)
# print(lst)

#数组末尾追加数组
# lst2 =  [90,100]
# lst.extend(lst2)
# print(lst)

#数组任意位置添加元素
# lst.insert(2,100)
# print(lst)

#数组切片替换
# lst3 = [101,102]
# lst[1:] = lst3
# print(lst)

#remove移除指定元素,如果有重复元素只移除第一个元素
# lst.remove(20)
# print(lst)

#pop删除指定索引的元素，如果不写索引则删除末尾元素
# lst.pop(1)
# print(lst)
# lst.pop()
# print(lst)

#clear清空数组
# lst.clear()
# print(lst)

#del删除数组对象
# del lst
# print(lst) #数组对象报错

#指定索引修改
# lst[2] = 100
# print(lst)

#切片修改多个值
# lst[1:3] = [100,200,300]
# print(lst)

#排序sort
# lst.sort() #升序
# print(lst)
# lst.sort(reverse=True) #降序
# print(lst)

#排序sorted,生成新数组
# lst2 = sorted(lst) #升序
# print(lst2)
# lst2 = sorted(lst,reverse=True) #降序
# print(lst2)

#列表生成式
# lst = [i for i in range(10)]
# print(lst)