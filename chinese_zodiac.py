chineseZodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
#从第0个开始访问4个元素
#print(chineseZodiac[0:4])
#从末尾开始访问倒数第一个元素
#print(chineseZodiac[-1])

year = 2020
print(year%12)
print(chineseZodiac[year%12])
#字符串的切片操作符
print(chineseZodiac[0:4])
#字符串的成员关系操作符
print('狗' not in chineseZodiac)
#字符串的连接
print(chineseZodiac+chineseZodiac)
#字符串的重复操作
print(chineseZodiac*3)