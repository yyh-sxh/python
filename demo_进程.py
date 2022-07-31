#引入包
#多进程
import multiprocessing
import time
import os

def dance(name,age):
    print(name,age)
    print('跳舞中。。。')
    time.sleep(0.2)

def sing(name,age):
    print('唱歌中。。。')
    print(name, age)
    time.sleep(0.2)
    sing_process_id = os.getpid() #获取进程编号
    os.kill(sing_process_id,9) #强制杀死进程

def my():
    print('演唱会开始')
if __name__ == '__main__':

    dance_process = multiprocessing.Process(target=dance,args=('张三',20))
    sing_process = multiprocessing.Process(target=sing,kwargs={'name':'李四','age':20})

    dance_process.start()
    # dance_process.join() #等待进程执行完成
    sing_process.start()
    # sing_process.daemon = True #主进程退出子进程直接销毁
    # sing_process.terminate() #退出主进程之前，子进程先销毁
    my()