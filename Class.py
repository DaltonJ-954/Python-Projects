class name:
    def __init__(self, firstName, lastName):
        #Initializing values for future objects created from this class
        self.firstName = firstName
        self.lastName = lastName
    def printName(self):
        print("Hello, I am {0} {1}".format(self.firstName, self.lastName))
        
def this(backwards):
    return backwards[::-1]
    
def speech(backwards):
    return backwards[::-1]

this_chat = this('I love spending time with family on all major holidays!')

mySpeech = speech('Make America great again!')

print(this_chat)
print(mySpeech)


#Passing in the actual object values
person = name('Dalton', 'Walls')
person.printName()
