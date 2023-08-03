

# Parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon_Based {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg



# Child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arm = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreating a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg


# Second child class instance
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg

# Thrid child class instance
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms!"
        return msg
    
# Fourth child class instance
class Alien(Organism):
    name = "Reptillian"
    species = "Unkown"
    legs = 2
    arms = 2
    dna = "Sequence X-01199"
    origin = "Universe"

    def technology(self):
        msg = "\nAs the gigantic ship lands, time slowed down and gravity was at zero. We are helpless to there capabilities."
        return msg


if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacterium = Bacterium()
    print(bacterium.information())
    print(bacterium.replication())

    alien = Alien()
    print(alien.information())
    print(alien.technology())