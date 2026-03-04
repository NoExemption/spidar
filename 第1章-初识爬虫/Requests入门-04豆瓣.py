import requests

url = "https://movie.douban.com/j/search_subjects"

#重新封装参数
param = {
    "type": "movie",
    "tag": "热门",
    "page_limit": 50,
    "page_start": 50,
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KhTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}
resp = requests.get(url=url, params=param, headers=headers)

print(resp.json())
resp.close()  #关掉resp