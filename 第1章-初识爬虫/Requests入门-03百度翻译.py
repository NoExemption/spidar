import requests

url = "https://fanyi.baidu.com/sug"

word = input("输入你想查询的英语单词")
dat = {
    "kw": word
}

#发送参数请求
resp = requests.post(url,data=dat)
print(resp.json())  #将服务器返回的内容直接处理成json() => dict
resp.close()