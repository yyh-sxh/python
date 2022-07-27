#模块包含的东西
import schedule


def fun():
    print('跑步')

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('吃东西')

a = 10
b = 20
sum = a + b


#import导入方式只能导入模块或者包
import math  #标准算术运算函数的标准库
# print(dir(math))
# print(math.pow(2,3))
# print(math.ceil(7.7777)) #7,向上取整
# print(math.floor(3.5333)) #3,向下取整

from math import pow #导入单个函数
# print(pow(2,3))

#from...import...可以导入所有东西
#导入自定义模块
from demo1 import add
# print(add(10,20))

#导入包，目录下含有__int__.py的目录叫做包，as添加别名
import page.module as module
# print(module.name)

# if __name__ == '__main__':  #以主程序运行时才会执行
#     print(add(30,20))

import sys #系统
import time #时间
import os #系统服务
import calendar #日期相关
import urllib #读取网上（服务器）数据标准库
import json #用于json的序列化和反序列化
import re #用于字符中正则表达式的匹配和替换
import decimal #用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
import logging #提供灵活的记录事件、错误警告和调试信息等日志


#第三方包的安装与使用
#pip install 包名
import schedule as sch

def job():
    print('哈哈---')

#每三秒执行一次job函数
sch.every(3).seconds.do(job)
# sch.run_pending()
# while True:
#     schedule.run_pending()
#     time.sleep(1)