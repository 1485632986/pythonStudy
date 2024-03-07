# def main():
#     f = open('C:\\Users\\Administrator\\Desktop\\1.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()

def main():
    try:
        f1 = open('C:\\Users\\Administrator\\Desktop\\1.txt', 'a', encoding='utf-8')
        f1.write('Hello word')
        f1.close()
        f2 = open('C:\\Users\\Administrator\\Desktop\\1.txt', 'r', encoding='utf-8')
        print(f2.read())
    except FileNotFoundError:
        print('文件不存在')
    except PermissionError:
        print('没有权限')
    finally:
        if f2:
            f2.close()
        if f1:
            f1.close()

if __name__ == '__main__':
    main()