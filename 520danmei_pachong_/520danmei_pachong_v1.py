'''
Author: xiaomin
Date: 2020-03-10 09:08:48
LastEditTime: 2020-09-04 11:06:49
LastEditors: xiaomin
Description: 
FilePath: \520danmei_pachong_\520danmei_pachong_v1.py
'''
import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import requests
import random
import time
import asyncio

from bs4 import BeautifulSoup

async def get_content(url,data=None):
    header={
        'Accept':'*/*',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }

    timeout=random.choice(range(8,15))

    while True:
        try:
            req=requests.get(url=url,headers=header,timeout=timeout)
            req.encoding='UTF-8-SIG'
            break
        except Exception as e:
            print('3'+str(e))
            time.sleep(random.choice(range(8,15)))
    return req.text


'''获取具体章节内容'''
def get_chapter(html):
    bf=BeautifulSoup(html,'html.parser')
    texts=bf.find_all('div',{'class':'Readarea ReadAjax_content','id':'chaptercontent'})
    text=texts[0].text.replace('　　','\n\xa0\xa0\xa0\xa0')
    return text

'''获取页面小说标题'''
async def get_page(page_num):
    urls='http://www.520danmei.net/shuku/13-lastupdate-0-'+str(page_num)+'.html'
    html=await get_content(urls)
    bf=BeautifulSoup(html,'html.parser')
    titles=bf.select('.name')
    return titles

'''获取小说章节'''
async def get_page_novel(page_num,page_title,title_num):
    filename='./novellist/'+page_title[title_num].text.replace('/','').replace('*','').replace('|','')+'.txt'
    print('创建小说：%s'%page_title[title_num].text+'------page%s'%str(page_num))
    article_urls='http://www.520danmei.net'+page_title[title_num].get('href')+'all.html'
    html=await get_content(article_urls)
    bf=BeautifulSoup(html,'html.parser')
    chapters=bf.select('#chapterlist > p > a')
    return chapters,filename

async def get_chapter_content(chapter_content,chapter_num,filename):
    try:
        chapter_urls='http://www.520danmei.net'+chapter_content[chapter_num+1].get('href')
        html=await get_content(chapter_urls)
        print('正在写入第%s'%str(chapter_num+1)+'章')
        f=open(filename,'a',encoding='utf-8')
        f.write('\n'+str(chapter_num+1)+'、'+chapter_content[chapter_num+1].text)
        f.write('\n')
        f.write(get_chapter(html))
        f.close()
        print('写入完成')
    except Exception as e:
        print(e)
        time.sleep(random.choice(range(8,15)))

async def main(nums):
    for page_num in range(nums):
        page_title=await get_page(page_num)
        for title_num in range(len(page_title)):
            (chapter_content,filename)=await get_page_novel(page_num,page_title,title_num)
            task=asyncio.gather(*[get_chapter_content(chapter_content,chapter_num,filename) for chapter_num in range(len(chapter_content)-1)])
            # for chapter_num in range(len(chapter_content)-1):
            #    get_chapter_content(chapter_content,chapter_num)
            await task

asyncio.run(main(2))

# if __name__ == "__main__":
#     for i in range(0,2):
#         #控制列表页数
#         urls='http://www.520danmei.net/shuku/13-lastupdate-0-'+str(i)+'.html'
#         html=get_content(urls)
#         bf=BeautifulSoup(html,'html.parser')
#         titles=bf.select('.name')
#         for n in range(len(titles)):
#             filename='./novellist/'+titles[n].text.replace('/','').replace('*','').replace('|','')+'.txt'
#             print('创建小说：%s'%titles[n].text+'------page%s'%str(i))
#             article_urls='http://www.520danmei.net'+titles[n].get('href')+'all.html'
#             html=get_content(article_urls)
#             bf=BeautifulSoup(html,'html.parser')
#             chapters=bf.select('#chapterlist > p > a')
#             for m in range(len(chapters)-1):
#                 try:
#                     chapter_urls='http://www.520danmei.net'+chapters[m+1].get('href')
#                     html=get_content(chapter_urls)
#                     print('正在写入第%s'%str(m+1)+'章')
#                     f=open(filename,'a',encoding='utf-8')
#                     f.write('\n'+str(m+1)+'、'+chapters[m+1].text)
#                     f.write('\n')
#                     f.write(get_chapter(html))
#                     f.close()
#                     print('写入完成')
#                 except Exception as e:
#                     print(e)
#                     time.sleep(random.choice(range(8,15)))

    