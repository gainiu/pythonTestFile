'''
Author: xiaomin
Date: 2020-09-02 13:41:33
LastEditTime: 2020-09-02 15:22:08
LastEditors: xiaomin
Description: 
FilePath: \pythonTestFile\txt\feature.py
'''

import functools

#函数
def func(message):
    print('Got a message: {}'.format(message))
got_message=func
got_message('hello world1')

#函数作为入参
def get_message(message):
    return 'got a message: '+message
def root_call(func,message):
    print(func(message))
root_call(get_message,'hello world2')

#函数嵌套函数
def func1(message):
    def func2(message):
        print('got a message: {}'.format(message))
    return func2(message)
func1('hello world3')

#闭包
def fun3():
    def func4(message):
        print('got a message: {}'.format(message))
    return func4
a=fun3()
a('hello world4')

#装饰器的普通写法
def my_decorate(func5):
    def wrapper():
        print('wrapper of decorate')
        func5()
    return wrapper
def greet():
    print('got a message: hello world5')
b=my_decorate(greet)
b()

#装饰器写法
def my_decorate1(func6):
    def wrapper1():
        print('wrapper of decorate1')
        func6()
    return wrapper1
@my_decorate1
def greet1():
    print('got a message: hello world6')
greet1()

#带参数的装饰器
def my_decorate2(func7):
    def wrapper2(message):
        print('wrapper of decorate2')
        func7(message)
    return wrapper2
@my_decorate2
def greet2(message):
    print('got a message: {}'.format(message))
greet2('hello world7')

#带多个参数的装饰器
def my_decorate3(func8):
    def wrapper3(*args,**kwargs):
        print('wrapper of decorate3')
        func8(*args,**kwargs)
    return wrapper3
@my_decorate3
def greet3(*args,**kwargs):
    print('got a message: {},{}'.format(*args,**kwargs))
greet3('hello world8','hello world9')

#带有自定义参数的装饰器
def repeat(num):
    def my_decorate4(func9):
        @functools.wraps(func9)#内置装饰器，将原函数的元信息，拷贝到对应的装饰器函数里
        def wrapper4(*args,**kwargs):
            for i in range(num):
                print('wrapper of decorate-{}'.format(i))
                func9(*args,**kwargs)
        return wrapper4
    return my_decorate4
@repeat(4)
def greet4(*args,**kwargs):
    print('got a message: {},{}'.format(*args,**kwargs))
greet4('hello world10','hello world11')
print(greet4.__name__)
help(greet4)

#类装饰器
class Count:
    def __init__(self,func10):
        self.func10=func10
        self.num_call=0

    def __call__(self,*args):
        self.num_call+=1
        print('num of call is : {}'.format(self.num_call))
        return self.func10(*args)
@Count
def example():
    print('hello world')
example()
example()
example()

#装饰器的嵌套
def my_decorate5(func11):
    def wrapper5():
        print('my_decorate5')
        func11()
    return wrapper5
def my_decorate6(func11):
    def wrapper6():
        print('my_decorate6')
        func11()
    return wrapper6
@my_decorate5
@my_decorate6
def greet5():
    print('WOWOWOWO')
greet5()
