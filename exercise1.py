#3 变量
#变量的定义和使用
# rmb = lambda dol,exrate: dol*exrate
# print('兑换的人民币是 %s ￥'%(rmb(100,6.9279)))

#4序列
#练习一 字符串
# str1 = 'Hello Python'
# str2 = 'Let\'s go'
# str3 = '"The Zen of Python" -- by Tim Peters '
# print(str1)
# print(str2)
# print(str3)
#练习二 字符串的基本操作
# import re
# str4 = 'xyz'
# str5 = 'abc'
# print(str4+str5)
# print(str4[1]+str4[2])
# for i in range(1,11):
#     print(str5)
# print(str5*10)
# print('a' in str4)
# print('a' in str5)
# num = re.findall('a',str5)
# print(num)
#练习三 列表的基本操作
# ali = [1,2,3,4,5]
# ali.append(100)
# ali.remove(1)
# print(ali)
# print(ali[0:3])#切片操作
# print(ali[-1])
#练习四 元组的基本操作
# tup = (1,2,3,4,5)
# # tup.append(1)
# print(tup[-1])
# tup2 = (7,8,9)
# print(tup+tup2)
# print(len(tup+tup2))
# print((tup+tup2).__len__())

#5条件和循环
#练习一 条件语句的使用
# str6 = 'abc'
# if len(str6)==10:
#     print('字符串 %s 的长度等于10'%str6)
# else:
#     print('字符串 %s 的长度等于 %d'%(str6,len(str6)))
# if not len(str6) == 10:
#     print('字符串长度不为10')
# else:
#     print('字符串长度为10')
# try:
#     num = int(input('请输入1-40之间的数字：'))
#     if 1<=num<=10:
#         print('输入范围在1-10')
#     elif 10<num<=20:
#         print('输入范围在11-20')
#     elif 20<num<=30:
#         print('输入范围在21-30')
#     elif 30<num<=40:
#         print('输入范围在31-40')
#     else:
#         print('输入数字不在范围内')
# except ValueError:
#     print('输入字符类型错误')
#练习二 循环语句的使用
# for i in range(2,100,2):
#     print(i)
# bli = [i for i in range(1,100) if(i%2==0)]
# print(bli)
# i = 1
# while i<100:
#     if i%3==0:
#         print(i)
#     i+=1

#6映射和集合
#练习一 字典的使用
# dict1 = {'a':1,'b':'hhh','c':3,'d':'第'}
# dict1['c']='cake'
# print(dict1)
# print(dict1['d'])
#练习二 集合的使用
# str7 = 'hello'
# print(set(str7))

#7文件和输入输出
# import datetime
# f = open('exercise.txt','w')
# f.write(datetime.datetime.now().strftime('%Y-%m-%d'))
# f = open('exercise.txt')
# print(f.read(4))
# f.close()

#9函数
# def add():
#     num = input('请输入多个数字，并用空格隔开:')
#     cli = num.split(' ')
#     addNum = 0
#     for i in cli:
#         addNum+=int(i)
#     print(addNum)
# add()
# def func1():
#     two_num = input('请输入两个数字，用空格做分隔：')
#     # 检查用户输入是否合法
#     func2(two_num)
#     num1, *_, num2 = list(two_num)
#     print(int(num1) + int(num2))
# def func2(check_number):
#     pass
# func1()
# def compare(*num):
#     dli = list(num)
#     print('最大的数为 %s'%max(dli))
#     print('最小的数为 %s'%min(dli))
# compare(1,23,45,2,34,56,7,54,6,65)
# def factorial(n):
#     def nei(i=1,j=1):
#         if j==n:
#             return i*j
#         return nei(i*j,j+1)
#     return nei
# num = factorial(5)
# print(num())
# def factorial(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return n*factorial(n-1)
# print(factorial(5))
# from functools import reduce
# n = 5
# print(reduce(lambda x,y: x*y ,range(1,n+1)))

#11装饰器
#练习一 定义装饰器，用于打印函数执行的时间
# import time
# import signal
#windows系统无法使用signal.alarm
# def runTime(func):
#     def nei():
#         def handler(singnum,frame):
#             raise TimeoutError('timer expired')
#         signal.signal(signal.SIGALRM,handler)
#         signal.alarm()
#         startTime = time.time()
#         func()
#         endTime = time.time()
#         print('use %s seconds'%(endTime-startTime))
#     return nei 
# @runTime
# def sleepTime():
#     time.sleep(3)
# sleepTime()
#练习二 定义装饰器，实现不同颜色显示执行结果的功能
import sys
def make_color(code):
    def decorator(func):
        def color_func(s):
            if not sys.stdout.isatty():
                return func(s)
            tpl = '\x1b[{}m{}\x1b[0m'
            return tpl.format(code, func(s))
        return color_func
    return decorator
@make_color(33)
def fmta(s):
    return '{:^7}'.format(str(float(s) * 1000)[:5] + 'ms')
print(fmta(5))
