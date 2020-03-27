#元组定义后不可修改
zodiacName = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
zodiacDays = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))

#用户输入月份和日期，并转成int类型
userMonth = int(input('请输入你的出生月份：'))
userDay = int(input('请输入你的出生日期：'))

#使用for循环判断
# for zdNum in range(len(zodiacDays)):
#     if zodiacDays[zdNum] >= (userMonth,userDay):
#         print(zodiacName[zdNum])
#         break
#     elif userMonth == 12 and userDay >23:
#         print(zodiacName[0])
#         break

#使用while循环判断
n = 0
while zodiacDays[n]<(userMonth,userDay):
    if userMonth == 12 and userDay >23:
        break
    n+=1
print(zodiacName[n])

# zodiacDay = filter(lambda x: x<(month,day),zodiacDays)
# #print(list(zodiacDay))
# zodiacLen = len(list(zodiacDay))%12
# print(zodiacName[zodiacLen])

