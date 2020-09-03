'''
Author: xiaomin
Date: 2020-09-02 17:40:25
LastEditTime: 2020-09-03 11:33:26
LastEditors: xiaomin
Description: 
FilePath: \pythonTestFile\iterable.py
'''
def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False

params=[1234,
        '1234',
        [1, 2, 3, 4],
        set([1, 2, 3, 4]),
        {1:1, 2:2, 3:3, 4:4},
        (1, 2, 3, 4)]

for param in params:
    print('{} is iterable? {}'.format(param,is_iterable(param)))

def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1
gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)

def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)
get_sum(8)

def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result
print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))

def index_normal1(L,target):
    for i,num in enumerate(L):
        if num==target:
            yield i
print(list(index_normal1([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))


def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)
print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))

