#encoding=UTF-8 #设置编码格式GBK、UTF-8等

#文件的读写操作，内置函数open
#file = open(filename,[mode,encoding]) #mode:r/w/a/b/+(读/写/追加/二进制方式打开文件/读写模式)，encoding编码,
# 使用二进制打开文件时需跟r或者w一起使用：rb/wb,使用读写模式也需跟其他模式一起使用a+
file = open('a.txt','a+',encoding='utf-8')
# print(file.readlines())


#文件的常用方法
# print(file.read()) #read([size])读取文件中size个字符，不写参数则从头读到尾
# print(file.readline()) #从文件中读取一行内容
# print(file.readlines()) #把文本中的每一行当做一个字符串对象，放入数组中返回
# file.write('广西') #替换文件中的内容
# file.writelines(list) #将字符串数组写入文件中，不添加换行
# print(file.tell()) #返回文件当前指针位置
# file.flush() #把缓冲区的内容写入文件，但不关闭文件
file.close() #把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源

#with，离开上下文管理器自动释放资源，操作文件推荐使用
# with open('a.txt','r',encoding='utf-8') as file1:
#     print(file1.read())

#文件复制
# with open('a.txt','rb') as str1:
#     with open('b.txt','wb') as str2:
#         str2.write(str1.read())

#os模块
import os
# os.system('notepad.exe') #打开系统应用程序
# os.startfile('D:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe') #打开可执行文件

#os模块相关函数
# os.getcwd() #返回当前的工作目录
# os.listdir(path) #返回指定路径下的文件和目录信息
# os.mkdir() #创建目录
# os.makedirs(path1/path2...) #创建多级目录
# os.rmdir(path) #删除目录
# os.removedirs(path1/path2...) #删除多级目录
# os.chdir(path) #将path设置为当前工作目录