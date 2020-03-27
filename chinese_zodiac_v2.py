chineseZodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# year = int(input('请用户输入出生年份'))

# print(chineseZodiac[year%12])

# for cz in chineseZodiac:
#     print(cz)

# #for i in range(13):
#  #   print(i)

# for year in range(2000,2021):
#     print('%s 年的生肖是 %s' %(year,chineseZodiac[year%12]))

import time
num = 5
while True:
    print(num)
    num=num+1
    if num > 10:
        break
    time.sleep(1)