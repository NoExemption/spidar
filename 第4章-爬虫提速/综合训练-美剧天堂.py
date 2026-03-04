"""
流程：
    1.拿到播放页面源代码
    2.从源代码当中提取到m3u8的url
    3.下载m3u8
    4.读取m3u8文件，下载视频
    5.合并视频
"""
import requests

"""
import requests
import re

obj = re.compile(r'url: "(?P<url>.*?)",',re.S)  # 用来提取m3u8的url地址

url = "https://www.meijutv.la/play/18252-1-1.html"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers=headers)
resp.close()

short_url = obj.search(resp.text).group("url")  # 拿到m3u8的地址
m3u8_url = "https:" + short_url
resp2 = requests.get(m3u8_url)
with open("无耻之徒第十一季第01集.m3u8",mode="wb") as f:
    f.write(resp2.content)
resp2.close()
print("下载完毕！")
"""

n = 1
with open("无耻之徒第十一季第01集.m3u8",mode="r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 去掉空格,空白和换行符
        if line.startswith("#"):  # 如果以#开头，则跳过，继续筛选下一行
            continue

        # 下载视频片段,使用多线程,多进程,协程提高效率
        resp3 = requests.get(line)
        with open(f"无耻之徒/{n}.ts",mode="wb") as ts_file:
            ts_file.write(resp3.content)
        print(f"完成了第{n}个片段的下载！")
        n += 1
        resp3.close()
