#创建对象
scores = {
    'name': '张三',
    'age': 18,
    'sex': '男'
}
# print(scores)

#对象值获取
# print(scores['name'])
# print(scores.get('name'))

#key的判断
# print('name' in scores) #True
# print('name' not in scores) #False

#删除指定的键值
# del scores['name']
# print(scores)

#对象清空
# scores.clear()
# print(scores)

#添加键值
# scores['name'] = '李四'
# print(scores)

#获取对象视图的三个方法
# kyes = scores.keys()
# print(kyes)
# values = scores.values()
# print(values)
# items = scores.items()
# print(items)

#编辑对象
# for item in scores:
#     print(item,scores[item],scores.get(item))

#对象生成式
items = ['name','age','sex']
values = ['张三',23,'男']
obj = { item: val for item,val in zip(items,values)}
print(obj)