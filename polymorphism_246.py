# Parent class MyCompany

class MyCompany:
    name = "Kieth Richter"
    contract = "MartBrow2223"
    password = "954_MB46"


    def SignOn(self):
        comp_name = input("Enter your name")
        contract_num = input("Enter the company contract number: ")
        comp_password = input("Please enter your password: ")
        if (contract_num == self.contract and comp_password == self.password):
            print("Manager log in initiated for {}. Select option.".format(comp.name))
        else:
            print("Incorrect managerID entry, please try again!")

# This is the child class Client
class Client(MyCompany):
    deliveries = "5 per month"
    accountName = "McDonalds"
    bill = 346,611,300.00
    pin_code = "72109898"

    # This child class uses the same methods as the MyConpany,
    #only difference is that a client code is used instead of the manager ID input from the parent class

    def LogIn(self):
        comp_name = input("Enter your name")
        contract_num = input("Enter the company contract number: ")
        clientPin = input("Please enter your client pin: ")
        if (contract_num == self.contract and clientPin == self.pin_code):
            print("Welcome back {}! Select from these options.".format(accountName))
        else:
            print("You have entered an incorrect code, enter correct code")

        # This code bellow summons the methods inside each class of parent and child

        supplier = MyCompany()
        supplier.SignOn()

        GM = Client()
        GM.LogIn()
