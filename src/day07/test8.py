# # import os
# # import time
# # def main():
# #     content = '北京欢迎你为你开天辟地…………'
# #     while True:
# #         # 清理屏幕上的输出
# #         os.system('cls')  # os.system('clear')
# #         print(content)
# #         # 休眠200毫秒
# #         time.sleep(0.2)
# #         content = content[1:] + content[0]
# # if __name__ == '__main__':
# #     main()
#
# import random
# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#     :param code_len: 验证码的长度(默认4个字符)
#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code
#
# if __name__ == '__main__':
#     code = generate_code(4)
#     print(code)

def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()
if __name__ == '__main__':
    main()