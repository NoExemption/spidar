import requests
import re

# 拿到页面源代码resp.text
url = "http://www.dytt89.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
resp = requests.get(url, verify=False, headers=headers)  # verify=False去掉安全验证
resp.encoding = 'gb2312'  # 指定字符集
resp.close()

# 拿到ul里面的li
obj1 = re.compile(r"2025必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<name>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">magnet', re.S)
result1 = obj1.finditer(resp.text)
child_href_list = []
for i in result1:
    ul = i.group("ul")

    # 提取子页面的链接
    result2 = obj2.finditer(ul)
    for it in result2:
        # 拼接子页面的url链接： 域名 + 子页面地址
        child_href = url + it.group("href").strip("/")
        child_href_list.append(child_href)  # 把子页面链接保存到列表child_href_list

# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href, verify=False, headers=headers)
    child_resp.encoding = 'gb2312'
    child_resp.close()
    result3 = obj3.search(child_resp.text)
    print(result3.group("name"))
    print(result3.group("download"))
    # break  # 测试时使用,仅输出第一个
