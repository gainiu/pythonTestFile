import time
import asyncio
import datetime
import requests
from bs4 import BeautifulSoup

async def get_content(i):
    move_name=i.select('.intro>h3>a')[0].text
    move_date=i.select('.dt')[0].text
    move_image=i.select('img')[0].get('src')
    print('{},{},{}'.format(move_name,move_date,move_image))
    # await asyncio.sleep(1)

async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    head={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'Referer':'https://time.geekbang.org/column/article/101855',
    'Connection':'keep-alive'}

    initpage=requests.get(url,headers=head).content
    initsoup=BeautifulSoup(initpage,'lxml')
    page_content=initsoup.select('div[id="showing-soon"]')

    task=asyncio.gather(*[get_content(i) for i in page_content[0].select('.item')])
    await task

start=datetime.datetime.now()
asyncio.run(main())
end=datetime.datetime.now()
print('wait time: {}'.format((end-start).microseconds))