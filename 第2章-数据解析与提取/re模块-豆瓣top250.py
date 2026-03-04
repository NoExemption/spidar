import requests
import re
import csv

# 获取页面源代码

for it in range(0,225,25):
    url = f"https://movie.douban.com/top250?start={it}&filter="
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)

    page_content = resp.text
    resp.close()

    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;'
                     r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<num>.*?)</span>', re.S)

    result = obj.finditer(page_content)
    f = open("data.csv",mode="a",encoding="utf-8",newline="") #newline=""消去csv文件里面的空白行
    csvwriter = csv.writer(f)
    for i in result:
        # print(i.group("name"))
        # print(i.group("year").strip())  # .strip()去除year前面的空格
        # print(i.group("score"))
        # print(i.group("num"))
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    f.close()
    print("over!")