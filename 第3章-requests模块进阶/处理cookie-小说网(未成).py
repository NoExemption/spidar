# 登录 -> 得到cookie
# 带着cookie去请求到书架的url -> 书架上的内容

# 必须把上面的两个操作连起来
# 我们可以使用session进行请求 -> session可以认为是一连串的请求，在这个过程中的cookie不会丢失
import requests

# 会话
session = requests.session()
data = {
    "username":" shameless11291219",
    "password":" shame11291219."
}

# 登录
url = "https://www.biquge95.com/login/"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
resp = session.post(url,data=data,headers=headers)
print(resp.text)
resp.close()