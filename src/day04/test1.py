"""
正整数的反转
Version: 0.1
Author: 骆昊
"""
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    # 该函数的功能是将变量num除以10并赋值给num，即num = num // 10
    num //= 10
print(reversed_num)
