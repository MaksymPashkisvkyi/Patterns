from abc import ABCMeta, abstractmethod


class IIterator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def has_next():
        pass

    @staticmethod
    @abstractmethod
    def next():
        pass


class IIterable(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def check():
        pass


class Queue(IIterator):

    def __init__(self, people):
        self.__index = 0
        self.__people = people

    def next(self):
        if self.__index < len(self.__people):
            people = self.__people[self.__index]
            self.__index += 1
            return people
        raise Exception("AtEndOfIteratorException", "At End of Iterator")

    def has_next(self):
        return self.__index < len(self.__people)


class Human(IIterable):

    def __init__(self, name):
        self.__name = name

    def check(self):
        print(f"This human has been checked. His name is {self.__name}")


if __name__ == '__main__':

    peoples = [Human("Jon"), Human("Ben"), Human("Mark"), Human("Bob")]
    queue = Queue(peoples)
    while queue.has_next():
        queue.next().check()
