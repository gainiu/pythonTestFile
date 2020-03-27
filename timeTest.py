import time
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d'))

import datetime
print(datetime.datetime.now())
newtime=datetime.timedelta(minutes=10)#设置时间偏移量
print(datetime.datetime.now()+newtime)

oneday=datetime.datetime(2020,2,30)
newtime=datetime.timedelta(days=2)
print(oneday+newtime)