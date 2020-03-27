import time

# print(time.time())
# time.sleep(3)

# def sleepTime():
#     time.sleep(3)

# startTime = time.time()
# sleepTime()
# endTime = time.time()
# print('use %s seconds'%(endTime-startTime))

#装饰器的定义
def Timmer(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        print('use %s seconds'%(endTime-startTime))
    return wrapper

@Timmer
def sleepTime():
    time.sleep(3)

# Timmer(sleepTime())
sleepTime()