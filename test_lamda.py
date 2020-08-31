'''
Author: xiaomin
Date: 2020-08-31 10:18:46
LastEditTime: 2020-08-31 11:34:32
LastEditors: xiaomin
Description: 
FilePath: \pythonTestFile\test_lamda.py
'''
print([(lambda x: x**2) (x) for x in range(10)])

squared=map(lambda x:x*2, [1,2,3,4,5])


d = {'mike': 10, 'lucy': 2, 'ben': 30}
newdict=sorted(d.items(), key=lambda x:x[1])
print(newdict)

