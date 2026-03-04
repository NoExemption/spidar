import requests
from lxml import etree

url = "https://www.zbj.com/fw/?k=saas"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers=headers)
resp.close()

html = etree.HTML(resp.text)

# 拿到每一个服务商的div
divs = html.xpath("/html/body/div[1]/div/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div")  # XPath默认不会将高度和宽度为 0 且overflow:hidden（元素不可见）的元素视为有效可交互元素，所以不会将其纳入计数;则复制xpath时div[2]需要修改成div[1]
n = 1
for div in divs:  # 每一个服务商的div
    price = div.xpath("./div/div[3]/div[1]/span/text()")[0]  # [0]是将列表里面的元素提取出来成字符串
    title = "saas".join(div.xpath("./div/div[3]/div[2]/a/span/text()"))
    com_name = div.xpath("./div/div[5]/div/div/div/text()")[0]
    print(f"第{n}个服务商")
    n += 1
    print(price,title,com_name)