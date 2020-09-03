'''
Author: xiaomin
Date: 2020-09-03 13:44:00
LastEditTime: 2020-09-03 13:44:24
LastEditors: xiaomin
Description: 
FilePath: \pythonTestFile\xiecheng.py
'''

import time

def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))

def main(urls):
    for url in urls:
        crawl_page(url)

main(['url_1', 'url_2', 'url_3', 'url_4'])
