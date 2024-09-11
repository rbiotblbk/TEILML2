from abc import ABC, abstractmethod


class MyBase(ABC):

    @abstractmethod
    def fetch_data(self):
        raise NotImplementedError

    def run2(self):
        print("I am running 1")


class MyRunner:
    def add(x, y):
        raise NotImplementedError

    def run2(self):
        print("I am running 2")


class OANDAApp(MyBase, MyRunner):

    def fetch_data(self):
        pass


class ISOApp(MyBase, MyRunner):

    def fetch_data(self):
        pass


iso = ISOApp()
iso.run2()
