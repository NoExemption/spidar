# 1.拿到contID(在url里面取得)
# 2.拿到videoStatus返回的json. -> srvURL
# 3.对srcURL里面的内容进行修整
# 4.下载视频
import requests

url = "https://pearvideo.com/video_1797785"
contID = url.split("_")[-1]

videoStatus = f"https://pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.5894668544843771"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    # 防盗链(引用页)：溯源，当前请求的上一级
    "referer":"https://pearvideo.com/video_1797785"
}
resp = requests.get(videoStatus,headers=headers)
dic = resp.json()
resp.close()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime,f"cont-{contID}")

# https://video.pearvideo.com/mp4/short/20241231/cont-1797785-16042954-hd.mp4
# https://video.pearvideo.com/mp4/short/20241231/1738996761849-16042954-hd.mp4

with open("2024年度回访：蔡磊坚信努力之后的希望.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)

print("over!")