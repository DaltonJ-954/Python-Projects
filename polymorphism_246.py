# Parent class MyCompany

class MyCompany:
    managerName = "Keith Richter"
    contract = "MartBrow2223"
    password = "954_MB46"


    def SignOn(self):
        comp_name = input("Enter your name: ")
        contract_num = input("Enter the company contract number: ")
        comp_password = input("Please enter your password: ")
        if (contract_num == self.contract and comp_password == self.password):
            print("Manager log in initiated for {}. Select option.".format(self.name))
        else:
            print("Incorrect managerID entry, please try again!")

# This is the child class Client
class Client(MyCompany):
    deliveries = "5 per month"
    accountName = "McDonalds"
    account_Num = "XSSTS00001212"
    bill = 346,611,300.00
    pin_code = "72109898"

    # This child class uses the same methods as the MyConpany,
    #only difference is that a client code is used instead of the manager ID input from the parent class

    def LogIn(self):
        account_name = input("Enter your account name: ")
        account_Num = input("Enter the account number: ")
        pin_code = input("Please enter your client pin: ")
        if (account_Num == self.account_Num and pin_code == self.pin_code):
            print("Welcome back {}! Select from these options.".format(self.accountName))
        else:
            print("You have entered an incorrect code, enter correct pin code")

class Employee(MyCompany):
    name = "Marvin Lane"
    email = "myLane@stummy.com"
    password = "marvin4520^^^"


    # This is the second child class
    
    def LogIn(self):
        empoyee_name = input("Enter your name: ")
        empoyee_email = input("Enter your email: ")
        empoyee_password = input("Please enter your password: ")
        if (empoyee_email == self.email and empoyee_password == self.password):
            print("Manager {} log in initiated for {}. Select option.".format(empoyee_name))
        else:
            print("Incorrect password entry, please try again!")


        # This code bellow summons the methods inside each class of parent and the two child classes

supplier = MyCompany()
supplier.SignOn()

GM = Client()
GM.LogIn()

Emp = Employee()
Emp.LogIn()
