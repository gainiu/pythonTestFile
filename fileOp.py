# #将小说的主要人物记录在文件中
# file1 = open('name.txt','w')#w表示write，写入
# file1.write('哈哈哈哈')
# file1.close()

# file2 = open('name.txt')
# print(file2.read())
# file2.close()

# file3 = open('name.txt','a')#a表示增加,如果用w会覆盖
# file3.write('诸葛亮')
# file3.close()

#逐行处理
# file4 = open('name.txt')
# for eachline in file4.readlines():
#     print(eachline)
#     print('=====')

file6 = open('name.txt')
print(file6.tell())#指针指向当前读取的位置
file6.read(1)#读取之后
print(file6.tell())#指针位置发生变化
#第一个参数代表偏移位置，第二个参数 0表示从文件头开始偏移 1表示从当前位置开始偏移 2从文件尾开始
file6.seek(5,0)
print(file6.tell())