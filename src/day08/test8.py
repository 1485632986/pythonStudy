from abc import ABCMeta, abstractmethod

#抽象类继承自object，可以使用metaclass=ABCMeta，也可以不继承自object，直接使用metaclass=ABCMeta，通过@abstactmethod装饰器
class Pet(object, metaclass=ABCMeta):
    """宠物"""
    def __init__(self, nickname):
        self._nickname = nickname
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass
class Dog(Pet):
    """狗"""
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)
class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)
def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()
if __name__ == '__main__':
    main()