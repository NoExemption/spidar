import requests

query = input("输入一个你喜欢的人物名称")

url = f'https://www.sogou.com/web?ie=UTF-8&query={query}'
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers=headers)  # 处理一个小反爬

print((resp))
print(resp.text)  # 拿到页面源代码
resp.close()