# sum = 0
# for i in range(11, 0, -2):
#     print('this i is:', i)
#     sum += i
#     print(sum)
import random

#
# sum1 = 0
# for i in range(0, 100, 2):
#     if sum1 % 2 == 0:
#         print("this is i %2 ==0:", i)
#         sum1 += i
#     elif sum1 % 2 == 1:
#         print("this is i %2 ==1:", i)
#         sum1 -= i
#     else:
#         print("this is i", sum1)
# print("sum is:", sum1)


# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     numbers = int(input("Enter numbers separated by: "))
#     if numbers == answer:
#         print("You got it right! numbers == answer", counter, "tries.")
#         break
#     elif numbers > answer:
#         print("You got it wrong! numbers > answer", counter, "tries.")
#     elif numbers < answer:
#         print("You got it wrong! numbers < answer", counter, "tries.")
# print("Thank you for playing!")


"""
输入两个正整数计算它们的最大公约数和最小公倍数
Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
# x = int(input('x = '))
# y = int(input('y = '))
# # 如果x大于y就交换x和y的值
# if x > y:
#     # 通过下面的操作将y的值赋给x, 将x的值赋给y
#     x, y = y, x
# # 从两个数中较的数开始做递减的循环
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break
# 如果上面的if语句中的条件都不满足, 则会执行下面的语句
# print('没有找到它们的最大公约数和最小公倍数')
# break语句会结束for循环
# break语句会结束while循环
# break语句会结束if语句
# break语句会结束try语句
# break语句会结束while语句
# break语句会结束for语句
# factor是变量

row = int(input("please input: "))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()