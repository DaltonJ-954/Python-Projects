from abc import ABC, abstractmethod


class Baseplane(ABC):

    @abstractmethod
    def fly(self):
        pass


class Jet(Baseplane):

    def fly(self):
        print("Flying")

jet = Jet()
jet.fly()
