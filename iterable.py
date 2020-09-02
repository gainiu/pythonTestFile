'''
Author: xiaomin
Date: 2020-09-02 17:40:25
LastEditTime: 2020-09-02 18:04:20
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
