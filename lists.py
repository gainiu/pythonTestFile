#数组
lists = [1,2,3,'a',5]
print(lists)
print(lists[0])
print(lists[4])

#修改数组第四个元素
lists[4] = 'b'
print(lists)

#数组末尾添加元素
lists.append('c')
print(lists)


#元组
tup1 = ('d','e','f','g')
tup2 = (6,7,8)

print(tup1)
print(tup1[0])
print(tup2[0:2])

#元组合并
tup3 = tup1 + tup2
print(tup3)

#元组删除
del tup3;

#元组复制
tup4 = ("hi!")
print(tup4 * 3)

#数组可以修改，元组不可变