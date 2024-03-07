from test4 import randoms

# randoms(3)

#初步构建代码块进行调用测试
def test1():
    #里层变量修改外层变量
    global a1
    a1 = 200
    d = 3
    print('this is test method',a1)
    def test2(b = 2):
        b = 2
        #里层变量修改外层变量
        nonlocal d
        d = 4
        print('this is test2 method param',b)
        print('d is',4)
    test2(300)
    print('test1 d is',d)

if __name__ == '__main__':
    a1 = 100
    test1();
    print('this is main method',a1)