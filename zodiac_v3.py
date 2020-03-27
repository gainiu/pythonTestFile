#元组定义后不可修改
chineseZodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiacName = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
zodiacDays = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))

#初始化生肖和星座的元组
# czNum = {}
# for i in chineseZodiac:
#     czNum[i]= 0
# zdNum = {}
# for i in zodiacName:
#     zdNum[i]= 0

czNum = {i:0 for i in chineseZodiac}
zdNum = {i:0 for i in zodiacName }

while True:
    #用户输入月份和日期，并转成int类型
    userYear = int(input('请输入你的出生年份：'))
    userMonth = int(input('请输入你的出生月份：'))
    userDay = int(input('请输入你的出生日期：'))

    #使用while循环判断
    n = 0
    while zodiacDays[n]<(userMonth,userDay):
        if userMonth == 12 and userDay >23:
            break
        n+=1
    print(zodiacName[n])

    print('%s 年的生肖是 %s' %(userYear,chineseZodiac[userYear%12]))

    czNum[chineseZodiac[userYear%12]]+=1
    zdNum[zodiacName[n]]+=1
    for eachKey in czNum.keys():
        print('生肖 %s 有 %d 个'%(eachKey,czNum[eachKey]))
    for eachKey in zdNum.keys():
        print('%s 有 %d 个'%(eachKey,zdNum[eachKey]))


