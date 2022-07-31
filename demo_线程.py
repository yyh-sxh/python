#线程，引入线程包
#互斥锁可以保证同一时刻只有一个线程去执行，能保证全局变量的数据没有问题
#线程等待和互斥锁把多任务改成单任务去执行，保证了数据的准确性，但执行性能会下降
import threading
lock = threading.Lock()
def sing():
    # 上锁
    lock.acquire()
    #获取当前线程
    current_thread = threading.current_thread()
    print(current_thread)
    print('唱歌')

    #执行完成之后释放锁，未释放锁，其他线程无法上锁只能等待
    lock.release()

def dance():
    print('跳舞')


if __name__ == '__main__':
    #获取主线程
    current_thread = threading.current_thread()
    print(current_thread)
    # 创建子线程
    sing_thread = threading.Thread(target=sing)
    sing_thread.start()
    sing_thread.join() #线程等待

    dancd_thread = threading.Thread(target=dance)
    dancd_thread.start()