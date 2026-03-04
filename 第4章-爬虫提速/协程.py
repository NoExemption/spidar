"""
import time

def func():
    print("饺子")
    time.sleep(3)  # 让当前的线程处于阻塞状态，CPU是不为我工作的
    print("布莱恩")

if __name__ == '__main__':
    func()
"""
import asyncio
import time

# input()程序也是处于阻塞状态
# requests.get("http://www.vegnet.com.cn/Price/List_p1.html") 在网络请求返回数据之前，程序也是处于阻塞状态的
# 一般情况下，当程序处于IO操作的时候，线程都会处于阻塞状态

# 协程：当程序遇见了IO操作的时候，可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，我们能看到的其实是多个任务一起在执行
# 多任务异步操作

"""
import asyncio
import time


# async def func():
#     print("你好啊，我叫皮特")
#
# if __name__ == '__main__':
#     g = func()  # 此时的函数是异步协程函数；此时函数执行得到的是一个协程对象
#     asyncio.run(g)  # 协程程序运行需要asyncio模块的支持

async def func1():
    print("你好啊，我叫皮特")
    # time.sleep(3)  # 当程序出现了同步操作时，异步就中断了
    await asyncio.sleep(3) # 异步操作的代码
    print("你好啊，我叫皮特s")

async def func2():
    print("你好啊，我叫阿Q")
    # time.sleep(2)
    await asyncio.sleep(2) # 异步操作的代码
    print("你好啊，我叫阿Qs")

async def func3():
    print("你好啊，我叫老乔")
    # time.sleep(4)
    await asyncio.sleep(4) # 异步操作的代码
    print("你好啊，我叫老乔s")

async def main():  # 在有运行的事件循环的环境中创建任务
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [
        asyncio.create_task(f1),asyncio.create_task(f2),asyncio.create_task(f3)
    ]
    await asyncio.wait(tasks)  # 一般await挂起操作放在协程对象前面    

if __name__ == '__main__':
    time1 = time.time()
    # 一次性启动后多个任务(协程)
    asyncio.run(main())
    time2 = time.time()
    print(f"总耗时：{time2-time1}秒")
"""


# 在爬虫领域的应用

# 定义异步下载函数
async def download(url):
    print(f"准备开始下载 {url}")
    await asyncio.sleep(2)  # 模拟网络请求
    print(f"{url} 下载完成")


# 定义主函数，负责管理多个下载任务
async def main():
    # 定义要下载的 URL 列表
    urls = [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]

    # 创建任务列表
    tasks = []
    for url in urls:
        # 将协程对象包装成任务对象
        task = asyncio.create_task(download(url))
        tasks.append(task)

    # 等待所有任务完成
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # 记录开始时间
    start_time = time.time()
    # 启动事件循环并执行主函数
    asyncio.run(main())
    # 记录结束时间
    end_time = time.time()
    # 计算并输出总耗时
    print(f"总耗时: {end_time - start_time} 秒")
