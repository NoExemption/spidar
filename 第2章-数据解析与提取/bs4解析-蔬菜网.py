import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.vegnet.com.cn/Price/list_ar510000.html?marketID=3"
headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers=headers)
resp.close()

f = open("菜价.csv",mode="w",encoding="utf-8",newline="")
csvwriter = csv.writer(f)

# 解析数据
# 1.将页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text,"html.parser")  # 指定html解析器
# 2.从bs对象中查找数据
# find(标签，属性=值),返回找到的第一个匹配元素
# find_all(标签，属性=值),返回所有匹配元素的列表
"""
div = page.find("div",class_="jxs_list price_l")  # class是python的关键字，需要再后面加"_"防止报错
"""
div = page.find("div",attrs={"class":"jxs_list price_l"})  # 和上一行作用相同
ps = div.find_all("p")[1:-1]
for p in ps:
    spans = p.find_all("span")
    date = spans[0].text
    kind = spans[1].text
    place = spans[2].text
    low = spans[3].text
    high = spans[4].text
    avg = spans[5].text
    unit = spans[6].text
    csvwriter.writerow([date,kind,place,low,high,avg,unit])

f.close()
print("over!")