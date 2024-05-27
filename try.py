


def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1,var2

def makeMoney():
    person = input("\nThis person needs to provide cash: ")
    person2 = input("\nThis person needs to combine his with person : ")
    return person,person2

def build():
    combine = True
    while combine:
        person1,person2 = makeMoney()
        try:
            person3 = int(person1) + int(person2)
            combine = False
        except ValueError as e:
            print("{}: \n\nYou did not provide a numeric value!".format(e))
        except:
            print("\n\nOpps, you provided an invalid input, progress will close now!")
    print("{} + {} + {}".format(person1,person2,person3))


def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print("{}: \n\nYou did not provide a numeric value!".format(e))
        except:
            print("\n\nOpps, you provided an invalid input, progress will close now!")
    print("{} + {} + {}".format(var1,var2,var3))




if __name__ == "__main__":
    compute()
