class Cat: 
    def __init__(self, pet):
        self.pet = pet
        self.__age = 10 # Private attributes/methods


    def print_age(self):
        print(self.age)

x = Cat('furry') # Defining class outside of the function
print(x.__dict__) # using dictionary method to show results of redefined class
print(x._Cat__age)
x._Cat__age = 3  # This shows that encapsulations can be changed with new result
print(x.__dict__)
print(x._Cat__age+7) # This shows that operators can be used to change private attributes as well 
