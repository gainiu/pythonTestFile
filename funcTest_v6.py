fd = open('TEST1\\txt\\name.txt',encoding='UTF-8')
try:
    for line in fd.readlines():
        print(line)
finally:
    fd.close()

#上下文管理器
with open('TEST1\\txt\\name.txt',encoding='UTF-8') as f:
    for line in f.readlines():
        print(line)
