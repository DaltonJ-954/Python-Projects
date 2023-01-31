from abc import ABC, abstractmethod


class Baseplane(ABC):  # The parent class
    def hover(self, flight):
        print("This fighter plane is swift while: ",flight)
# This function is passing an argument without any data that is called.

    @abstractmethod
    def fly(self, flight):
        pass

class Jet(Baseplane): # Child class
# We use the child define the behavior of the parent class's private attribute
    def fly(self, flight):
        print("Did you guys see how that rocket {} up into the atmosphere?".format(flight))

jet = Jet()
jet.hover("jetted")
jet.fly("jetted")
