import time

#装饰器的使用
def newTips(argv):
    def tips(func):
        def inner(a,b):
            print('start:%s %s'%(argv,func.__name__))
            func(a,b)
            print('end')
        return inner
    return tips
@newTips('add_module')
def add(a,b):
    print(a+b)
@newTips('sub_module')
def sub(a,b):
    print(a-b)


# add(2,3)
# sub(2,3)