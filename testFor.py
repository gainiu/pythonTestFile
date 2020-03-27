#从1到10的偶数的平方
aList=[]
for i in range(1,11):
    if(i%2==0):
        aList.append(i*i)
print(aList)

#列表推导式写法
bList = [i*i for i in range(1,11) if(i%2==0)]
print(bList)

zodiacName = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
#字典推导式初始化
zdNum = {i:0 for i in zodiacName }