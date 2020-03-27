# from urllib import request
import requests
import re

# url='http://www.baidu.com'
# response=request.urlopen(url,timeout=2)
# print(response.read().decode('utf-8'))

content=requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text

print(content)