class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s isPlaying' % self._name)

    def watch_tv(self):
        if self._age < 18:
            print('You need to be 18 or older to watch TV%s' % self._name)
        else:
            print('You can watch TV%s' % self._name)


class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self._grades = grades

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, grades):
        self._grades = grades

    def study(self, course_name):
        print('%s is studying %s' % (self._name, course_name))


class Teacher(Person):
    """老师"""
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('zhangsan',14,'chusan')
    stu.study("english")
    stu.watch_tv()

    t = Teacher('lisi', 20, '教授')
    t.teach("python")
    t.watch_tv()

if __name__ == '__main__':
    main()