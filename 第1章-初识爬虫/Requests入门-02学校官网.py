import requests

url = 'https://www.tjut.edu.cn/'
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers=headers)  # 处理一个小反爬
resp.encoding = "UTF-8"

print((resp))
print(resp.text)  # 拿到页面源代码
resp.close()