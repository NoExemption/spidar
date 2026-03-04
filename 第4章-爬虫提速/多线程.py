# 线程，进程
# 进程是资源单位，每一个进程至少要有一个线程
# 线程是执行单位

# 启动每一个程序默认都会有一个主线程

# 单线程
# def func():
#     for i in range(1000):
#         print("func",i)
#
# if True:
#     func()
#     for i in range(1000):
#         print("main",i)

# 多线程

# 第一种写法
from threading import Thread  # 线程类

def func(name):  # 多个子线程才需要增加"name"
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    t1 = Thread(target=func,args=("元始天尊",))  # 创建线程并给线程安排任务
    t1.start()  # 多线程状态为可以开始工作状态，具体的执行时间由CPU决定

    t2 = Thread(target=func,args=("灵宝天尊",))  # args=""传递参数必须是元组，所以要加逗号
    t2.start()

    for i in range(1000):
        print("main",i)  # 主线程是'for..."main",i)',func()是子线程


"""
# 第二种写法
from threading import Thread
class MyThread(Thread):
    def run(self):  # 固定使用run -> 当线程被执行的时候，被执行的就是run()
        for i in  range(1000):
            print("子线程",i)

if __name__ == '__main__':
    t =  MyThread()
    # t.run是方法的调用 -> 是单线程
    t.start()

    for i in range(1000):
        print("主线程",i)
"""