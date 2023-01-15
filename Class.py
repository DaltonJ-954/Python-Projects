class name:
    def __init__(self, firstName, lastName):
        #Initializing values for future objects created from this class
        self.firstName = firstName
        self.lastName = lastName
    def printName(self):
        print("Hello, I am {0} {1}".format(self,firstName,lastName))


#Passing in t he actual object values
person=name('Air', 'Jordan')
person.printName()
