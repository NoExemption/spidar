# requests.get() 同步的代码 -> 异步操作aiohttp

import asyncio
import aiohttp

urls = [
    "https://www.umei.cc/d/file/20230906/bec2a6b127c47b8d6f53f36e1a875f07.jpeg",
    "https://www.umei.cc/d/file/20230906/3ff61c3ea61f07c98fb3afd8aff40bf8.jpeg",
    "https://www.umei.cc/d/file/20230727/ccbeeb2ed427010ef5728e87f2d118ec.jpeg"
]

async def aiodownload(url):
    # 发送请求 -> 得到图片内容 -> 保存到文件
    # s = aiohttp.ClientSession() <==> requests ; s.get()/.post() <==> requests.get()/.post()
    name = url.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    async with aiohttp.ClientSession() as session:  # 使用with就不需要再手动关闭session或者resp
        async with session.get(url) as resp:
            # 写入文件
            with open("img2/"+name,mode="wb") as f:
                f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起
    print(name,"下载完成！")
async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(aiodownload(url))
        tasks.append(task)

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())