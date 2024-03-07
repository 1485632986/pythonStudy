# from src.day08.student import Student
#
#
# def main():
#     stu1 = Student('zhangsan', 18)
#     stu1.study('python')
#     stu1.watch()
#     stu2 = Student('lisi', 100)
#     stu2.study('java')
#     stu2.watch()
#
#
# if __name__ == '__main__':
#     main()
from src.day08.testClass import Test

# def main():
#     test = Test('hello')
#     # AttributeError: 'Test' object has no attribute '__bar'
#     test.__bar()
#     # AttributeError: 'Test' object has no attribute '__foo'
#     print(test.__foo)
def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)

if __name__ == "__main__":
    main()
