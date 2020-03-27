#用户输入abc后会有ValueError报错，可以捕获异常
# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('请输入数字')

#捕获多个异常情况处理
# except (ValueError,AttributeError,KeyError):

#把错误信息打印出来
# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print('0不能做除数：%s'%e)

#捕获全部的错误信息,打印错误信息
# try:
#     print(1/'a')
# except Exception as e:
#     print('%s'%e)

#异常处理的完整过程
try:
    a = open('name.txt')
except Exception as e:
    print('%s'%e)
finally:
    a.close()