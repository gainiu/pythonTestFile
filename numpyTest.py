import numpy as np

arr1=np.array([2,3,4])
print(arr1)
print(arr1.dtype)
print(arr1*10)

data = [[1,2,3],[4,5,6]]
arr2=np.array(data)
print(arr2)
print(arr2.dtype)

#矩阵
print(np.zeros((3,5)))
print(np.ones((4,6)))
print(np.empty((2,3,2)))

#numpy的切片操作
arr3=np.arange(10)
print(arr3[5:8])
arr3[5:8]=10
print(arr3)
arr3.sort()
print(arr3)

arr3_slice=arr3[5:8].copy()
arr3_slice[:]=100
print(arr3_slice)
print(arr3)