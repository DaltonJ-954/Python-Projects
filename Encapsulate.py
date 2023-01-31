class Cat: 
    def __init__(self, name, age, breed, gender):
        self.__name = name
        self.__age = age
        self._breed = breed
        self._gender = gender


    def setName(self, private):
        self.__name = private
    
    def getName(self):
        print(self.__name)


p1 = Cat("Shimmy", 5, 'bengal', 'F')
print(p1._breed) # This line and 20 are protected

p1._breed = "m"
print(p1._breed)
p1.getName() # This line is accessing the privte property
p1.setName("Laura")
p1.getName()
