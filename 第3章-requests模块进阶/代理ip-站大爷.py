import requests

# 61.141.226.225
proxies = {
    "https":"https//61.141.226.225"
}

resp = requests.get("http://www.baidu.com/",proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
resp.close()