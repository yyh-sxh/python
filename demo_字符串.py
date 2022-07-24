#字符串的驻留机制
a = 'python'
b = 'python'
# print(a,id(a))
# print(b,id(b))

#字符串拼接join,只new一次对象,效率比+高
a = ''.join([a,'hello'])
# print(a,id(a))

#字符串查询
str = 'hello world'
#index,查找子字符串第一次出现的位置，没有则抛出异常
print(str.index('e')) #1
# print(str.index('g')) #抛出异常

#rindex，查找子字符串最后一次出现的位置，没有则抛出异常
print(str.rindex('l')) #9

#find,查找子字符串第一次出现的位置，没有返回-1
print(str.find('e')) #1

#rfind,查找子字符串最后一次出现的位置，没有返回-1
print(str.rfind('l')) #9