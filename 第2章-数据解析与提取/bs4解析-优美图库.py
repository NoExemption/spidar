import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/weimeitupian/yijingtupian/"
ur = "https://www.umei.cc/"
resp = requests.get(url)
resp.encoding = "utf-8"
resp.close()

# 生成bs对象
page = BeautifulSoup(resp.text, "html.parser")

alist = page.find("div", class_="item_list infinite_scroll").find_all("a")
for a in alist:
    urls = ur + a.get("href").strip("/")

    # 拿到子页面的源代码
    child_page_resp = requests.get(urls)
    child_page_resp.encoding = "utf-8"
    child_page_resp.close()

    # 从子页面拿到图片的下载路径
    child_page = BeautifulSoup(child_page_resp.text, "html.parser")

    img = child_page.find("div", class_="big-pic").find("img")
    src = img.get("src")
    # 下载图片
    img_resp = requests.get(src)
    img_name = src.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    with open("img/"+img_name, mode="wb") as f:
        f.write(img_resp.content)  # img_resp.content拿到的是字节
    print("over!",img_name)
    time.sleep(1)

print("all over!")