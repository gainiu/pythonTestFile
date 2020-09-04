'''
Author: xiaomin
Date: 2020-03-10 09:08:48
LastEditTime: 2020-09-04 09:43:07
LastEditors: xiaomin
Description: 
FilePath: \520danmei_pachong_\520danmei_pachong.py
'''
import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import requests
import random
import time

from bs4 import BeautifulSoup

def get_content(url,data=None):

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

# def get_chaptertitle(ct):
#     bf=BeautifulSoup(ct,'html.parser')
#     texts=bf.select('#chapterlist > p > a').text


'''获取具体章节内容'''
def get_chapter(html):
    bf=BeautifulSoup(html,'html.parser')
    texts=bf.find_all('div',{'class':'Readarea ReadAjax_content','id':'chaptercontent'})
    text=texts[0].text.replace('　　','\n\xa0\xa0\xa0\xa0')
    return text




if __name__ == "__main__":
    for i in range(0,2):
        #控制列表页数
        urls='http://www.520danmei.net/shuku/13-lastupdate-0-'+str(i)+'.html'
        html=get_content(urls)
        bf=BeautifulSoup(html,'html.parser')
        titles=bf.select('.name') 
        for n in range(len(titles)):       
            filename='./novellist/'+titles[n].text.replace('/','').replace('*','').replace('|','')+'.txt'
            print('创建小说：%s'%titles[n].text+'------page%s'%str(i))
            article_urls='http://www.520danmei.net'+titles[n].get('href')+'all.html'
            html=get_content(article_urls)
            bf=BeautifulSoup(html,'html.parser')
            chapters=bf.select('#chapterlist > p > a')
            for m in range(len(chapters)-1):
                try:
                    chapter_urls='http://www.520danmei.net'+chapters[m+1].get('href')
                    html=get_content(chapter_urls)
                    print('正在写入第%s'%str(m+1)+'章')
                    f=open(filename,'a',encoding='utf-8')
                    f.write('\n'+str(m+1)+'、'+chapters[m+1].text)
                    f.write('\n')
                    f.write(get_chapter(html))
                    f.close()
                    print('写入完成')
                except Exception as e:
                    print(e)
                    time.sleep(random.choice(range(8,15)))

    # html=get_content(url)
    # get_chapter(html)
    