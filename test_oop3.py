'''
Author: xiaomin
Date: 2020-08-31 14:29:08
LastEditTime: 2020-08-31 14:36:16
LastEditors: xiaomin
Description: 
FilePath: \pythonTestFile\test_oop3.py
'''
class A():
    def __init__(self):
        print('start A')

class B(A):
    def __init__(self):
        print('start B')
        super().__init__()

class C(A):
    def __init__(self):
        print('start C')
        super().__init__()

class D(B,C):
    def __init__(self):
        print('start D')
        super().__init__()

D()