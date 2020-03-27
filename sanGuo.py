# #读取人物名字
# f = open('TEST1\\txt\\name.txt',encoding='UTF-8')
# data = f.read()
# print(data.split('|'))

# #读取兵器名字
# f2 = open('TEST1\\txt\\weapon.txt',encoding='UTF-8')
# # data2 = f2.read()
# i = 1
# for line in f2.readlines():
#     if i%2==1:
#         print(line.strip('\n'))#输出行内容并过滤掉结尾换行符
#     i+=1

# f3 = open('TEST1\\txt\\sanguo.txt',encoding='GB18030')
# print(f3.read().replace('\n',''))#把换行符替换成空

# #使用函数
# def func():
#     print(open('TEST1\\txt\\name.txt',encoding='UTF-8').read())
# #调用函数
# func()

#带参数的函数
def func(filename,encode):
    print(open(filename,encoding=encode).read())
func('TEST1\\txt\\name.txt','UTF-8')