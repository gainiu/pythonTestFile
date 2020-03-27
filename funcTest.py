# def func(a,b,c):
#     print('a= %s'%a)
#     print('b= %s'%b)
#     print('c= %s'%c)

# func(1,2,3)
# #指定参数关键字后可以忽略顺序
# func(1,c=3,b=2)

#当想传多个不确定个数参数时可以用*
# def howlong(first,*other):
#     print(len(first)+len(other))
# howlong('1','45','24','65')
# howlong('s','sd','sdd')

# var1 = 123
# def func():
#     var1 = 456#定义在函数内的变量只能作用于该函数内
#     print(var1)
# func()

# var2 = 123
# def funcg():
#     global var2
#     var2 = 456#添加global后变量为全局变量，作用于全局
# print(var2)
# funcg()

# for i in range(10,20,2):
#     print(i)

#使用迭代器yield节省系统资源
# def floatRange(start,stop,step):
#     x = start
#     while x<stop:
#         yield x
#         x+=step
# for i in floatRange(10,20,0.5):
#     print(i)

#简单函数可以使用lambda
# def add(x,y): return x+y
# add2 = lambda x,y:x+y
# print(add(1,2))
# print(add2(3,4))

#使用filter函数
# a=[1,2,3,4,5,6,7,8]
# b=list(filter(lambda x: x>3,a))
# print(b)

#使用map函数
# a=[1,2,3]
# b=list(map(lambda x: x+10,a))
# print(b)

#使用reduce函数
# from functools import reduce
# print(reduce(lambda x,y: x+y , [2,3,4],1))

# #使用zip函数
# for i in zip((1,2,3),(4,5,6)):
#     print(i)
# #使用zip函数将字典的key和value调换
# dicta = {'a':'1','b':'2'}
# dictb = zip(dicta.values(),dicta.keys())
# print(dict(dictb))

#闭包:外包函数的变量被内部函数引用
def sum(a):
    def add(b):
        return a+b
    return add
#返回add：函数名称或函数的引用
#返回add()：函数的调用
def func():
    a = 1
    b = 2
    return a+b
    
num1 = sum(1)
print(num1(2))

num2 = func()
# print(type(num1))#<class 'function'>
# print(type(num2))#<class 'int'>

