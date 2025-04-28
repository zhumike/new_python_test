#使用 threading 进行多线程操作:
#1.创建 threading.Thread 实例，调用其 start() 方法
# import time
# import threading
#
# def task_thread(counter):
#     print(f'线程名称：{threading.current_thread().name} 参数：{counter} 开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
#     num = counter
#     while num:
#         time.sleep(3)
#         num -= 1
#     print(f'线程名称：{threading.current_thread().name} 参数：{counter} 结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
#
#
# if __name__ == '__main__':
#     print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
#
#     #初始化3个线程，传递不同的参数
#     t1 = threading.Thread(target=task_thread, args=(3,))
#     t2 = threading.Thread(target=task_thread, args=(2,))
#     t3 = threading.Thread(target=task_thread, args=(1,))
#     #开启三个线程
#     t1.start()
#     t2.start()
#     t3.start()
#     #等待运行结束
#     t1.join()
#     t2.join()
#     t3.join()
#
#     print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')



#2.继承 Thread 类，在子类中重写 run() 和 init() 方法

import time
import threading


class MyThread(threading.Thread):
    def __init__(self, counter):
        super().__init__()
        self.counter = counter


    def run(self):

        print(
            f'线程名称：{threading.current_thread().name} 参数：{self.counter} 开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}'
        )
        counter = self.counter
        while counter:
            time.sleep(3)
            counter -= 1
        print(
            f'线程名称：{threading.current_thread().name} 参数：{self.counter} 结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}'
        )


if __name__ == "__main__":
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')

    # 初始化3个线程，传递不同的参数
    t1 = MyThread(3)
    t2 = MyThread(2)
    t3 = MyThread(1)
    # 开启三个线程
    t1.start()
    t2.start()
    t3.start()
    # 等待运行结束
    t1.join()
    t2.join()
    t3.join()

    print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')