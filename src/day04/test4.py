"""
输入M和N计算C(M,N)
Version: 0.1
Author: 骆昊
"""
from random import randint


# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# print('fm = {}'.format(fm))
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# print('fn = {}'.format(fn))
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# print('fm_n = {}'.format(fm_n))
# print(fm // fn // fm_n)
#
# print("==============================")
#
#
# def fan(nums):
#     res = 1
#     for i in range(1, nums + 1):
#         res *= i
#     print('res is:', res)
#     return res
#
#
# a = int(input('a = '))
# b = int(input('b = '))
# print(fan(a) // fan(b) // fan(a - b))


def randoms(test=2):
    total = 0
    print('this is random number', test)
    for _ in range(test):
        total += randint(1, 100)
    return total


def add(a=0, b=0, c=1):
    return a + b - c


if __name__ == '__main__':
    print('test4 print', randoms())
    print('test4 print random', randoms(3))
    print(add(1, 2, 3))
    print(add(c=50, a=100, b=200))
