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
# print(str.index('e')) #1
# print(str.index('g')) #抛出异常

#rindex，查找子字符串最后一次出现的位置，没有则抛出异常
# print(str.rindex('l')) #9

#find,查找子字符串第一次出现的位置，没有返回-1
# print(str.find('e')) #1

#rfind,查找子字符串最后一次出现的位置，没有返回-1
# print(str.rfind('l')) #9

#字符串大小写转换
#upper全部转换成大写
c = a.upper()
# print(c)

#lower全部转换成小写
d = c.lower()
# print(d)

#swapcase大写转小写、小写转大写
f = 'PYTHON hello'
# print(f.swapcase())

#capitalize第一个字符大写，其余小写
# print(f.capitalize())

#title每个单词首字母大写
# print(f.title())

#字符串对齐方式
#center居中对齐,第一个参数宽度，第二个参数填充符
# print(f.center(20,'*'))

#ljust左对齐，第一个参数宽度，第二个参数填充符
# print(f.ljust(20,'*'))

#rjust右对齐，第一个参数宽度，第二个参数填充符
# print(f.rjust(20,'*'))

#zfill右对齐,只有一个参数宽度，使用0填充
# print(f.zfill(20))

#字符串的分割
#split左分割、rsplit右分割
g = 'hello,world,python'
# print(g.split(sep=','))
# print(g.split(','))
# print(g.split(sep=',',maxsplit=1))
# print(g.split(',',1))

#字符串的判断
#isidentifier判断是否合法的标识符
# print('张三'.isidentifier()) #true

#isspace判断是否由空白字符组成，回车、换行、水平制表符
# print(''.isspace()) #false
# print(' '.isspace()) #true

#isalpha判断是否由字母组成
# print('hello'.isalpha()) #true
# print('张三'.isalpha()) #true
# print('张三1'.isalpha()) #false

#isnumeric判断是否由数字组成
# print('123'.isnumeric()) #true
# print('张三'.isnumeric()) #false
# print('张三1'.isnumeric()) #false

#判断是否由字母数字组成
# print('张三12'.isalnum()) #true
# print('张三&12'.isalnum()) #false

#字符串的连接
#join连接
lst = ['hello','world']
# print(','.join(lst))
lst2 = ('hello','world')
# print('|'.join(lst2))

#replace替换,第一个参数需要替换的字符，第二个参数替换字符，第三个参数替换个数
h = 'hello world'
i = h.replace('world','java')
# print(i)

#字符串的比较
#比较原理：比较ordinal value（原始值），内置函数ord(),chr()
#比较规则：第一个字符开始依次比较，直到两个字符串中的字符不相等时返回结果（布尔值），后续不再比较
#运算符：>,>=,<,<=,==,!=
# print('apple' > 'app') #true
# print('apple' > 'banana') # false

#字符串切片,产生新的字符串
s = 'helloworld'
# print(s[2:6])
# print(s[:6])
# print(s[3:])
# print(s[-4:])

#字符串格式化
# %占位符
name = '张三'
age = 18
# print('我叫%s，今年%d岁' % (name,age))
# print('%10d' % 99) #10表示宽度
# print('%.3f' % 3.1415926) #.3表示保留几位小数

# {}占位符
# print('我叫{0},今年{1}岁'.format (name,age))
# print(f'我叫{name},今年{age}岁')
# print('{0:.3}'.format(3.1415926)) #.3保留三位数
# print('{0:.3f}'.format(3.1415926)) #.3f表示保留三位小数

# 字符串编码、解码
#encode编码，默认utf-8
s = '天涯共此时'
print(s.encode())
# print(s.encode(encoding='GBK'))

#decode
byte = s.encode()
# print(byte.decode())