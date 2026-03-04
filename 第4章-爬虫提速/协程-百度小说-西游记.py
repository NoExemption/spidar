# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}  ->  所有章节的名称与cid
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}  ->  各章节的具体内容

import requests
import asyncio
import aiohttp
import aiofiles
import json

"""
1.同步操作：访问getCatalog,拿到所有章节的cid和名称
2.异步操作：访问getChapterContent,下载所有的文章内容
"""

async def aiodownload(cid,b_id,title):
    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofiles.open("西游记/"+title,mode="w",encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])


async def getCatalog(url):
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "cookie":"BAIDUID=3C47CE61B7BF1C5EC209EF358F3E76E1:FG=1; BAIDUID_BFESS=3C47CE61B7BF1C5EC209EF358F3E76E1:FG=1; BIDUPSID=3C47CE61B7BF1C5EC209EF358F3E76E1; PSTM=1739084932; ZFY=qxjEN2HzxYlgDrF6J66n5QNM30mX2Y3NVoFDsq1V3a4:C; H_PS_PSSID=60277_61027_61676_61986_62056_62061_62091_62109_62164_62168_62177_62185_62187_62180_62195; delPer=0; PSINO=1; BA_HECTOR=0lag8k202gal250g2g202g21b5g8m71jr0fip1v; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_bf1e478a71b02a743ab42bcfed9d1ff1=1739603455,1739603548; HMACCOUNT=B66668888F0AEC0D; Hm_lpvt_bf1e478a71b02a743ab42bcfed9d1ff1=1739604536"
    }
    resp = requests.get(url,headers=headers)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:  # item就是对应每一个章节的名称和cid
        title = item['title']
        cid = item['cid']
        task = asyncio.create_task(aiodownload(cid,b_id,title))
        tasks.append(task)
    resp.close()
    await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(getCatalog(url))
    print("全部下载完成!")