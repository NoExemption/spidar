# 1.提取单个页面的数据
# 2.上线程池，多个页面同时抓取
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("蔬菜价格行情.csv", mode="a", encoding="utf-8")
csvwriter = csv.writer(f)


def download_one_page(url):
    # 拿到页面源代码
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    resp.close()

    html = etree.HTML(resp.text)
    div = html.xpath("/html/body/div[3]/div[2]/div/div[1]")[
        0]  # XPath默认不会将高度和宽度为 0 且overflow:hidden（元素不可见）的元素视为有效可交互元素，所以不会将其纳入计数;则复制xpath时div[4]需要修改成div[3]
    ps = div.xpath("./p")
    for p in ps:
        span = p.xpath("./span/text()")
        a = p.xpath("./span/a/text()")
        # 把数据存放在文件中
        row = span + a
        csvwriter.writerow(row)

    print(url, "提取完毕！")


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 500):
            # 把下载任务提交给线程池
            t.submit(download_one_page, f"http://www.vegnet.com.cn/Price/List_p{i}.html")
    f.close()  # 所有线程执行完毕之后，保证在所有数据都写入文件后再关闭文件
    print("全部提取完毕！")
