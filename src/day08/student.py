class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s" % (self.name, course_name))

    def watch(self):
        if self.age <= 18:
            print("%s正在看《熊出没》" % self.name)
        else:
            print("%s正在看《独步天下》" % self.name)

def main():
    stu1 = Student('zhangsan', 18)
    stu1.study('python')
    stu1.watch()
    stu2 = Student('lisi', 100)
    stu2.study('java')
    stu2.watch()


if __name__ == '__main__':
    main()