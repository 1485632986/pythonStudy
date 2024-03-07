# 生成器
def fid(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for add in fid(10):
        print(add)


if __name__ == '__main__':
    main()