#集合的创建,集合不允许重复,集合是无序的
s = {1,2,3,4,5,5,6,6}
# print(s) #123456

s1 = set(range(6))
# print(s1) #012345

s2 = set([1,2,3,4,5])
# print(s2) #12345

s3 = set(('python','hello'))
# print(s3)

s4 = set('python')
# print(s4)

#元素判断
# print(10 in s) #false
# print(1 in s) #true

#集合添加
#添加单个add
s.add(10)
# print(s)

#添加多个update
s.update({11,12})
# print(s)
s.update([13,14])
# print(s)

#集合删除
#remove指定一个元素,元素不存在抛出异常
s.remove(1)
# print(s)

#discard指定删除一个元素，不抛出异常，比remove好
s.discard(2)
# print(s)

#pop删除随机一个元素,没有参数
s.pop()
# print(s)

#clear清空集合
s.clear()
# print(s)

#集合之间的关系
#两个集合是否相等,元素相同就相等，跟顺序无关
s5 = {10,20,30,40}
s6 = {20,30,40}
# print(s5 == s6) #false
# print(s5 != s6) #true

#子集issubset
# print(s5.issubset(s6)) #false
# print(s6.issubset(s5)) #true

#超集
# print(s5.issuperset(s6)) #true
# print(s6.issuperset(s5)) #false

#交集,有交集为false
# print(s5.isdisjoint(s6)) #false
# print(s6.isdisjoint(s5)) #false

#集合操作
#交集
# print(s5.intersection(s6)) #40,30,20
# print(s5&s6) #40,30,20

#并集
# print(s5.union(s6)) #10,20,30,40
# print(s5|s6)

#差集
# print(s5.difference(s6)) #10
# print(s5-s6)

#对称差集
s7 = {10,20,30}
s8 = {20,40}
# print(s7.symmetric_difference(s8)) #10,30,40
# print(s7^s8)

#集合生成式
s9 = { i for i in range(5)}
# print(s9) #1,2,3,4