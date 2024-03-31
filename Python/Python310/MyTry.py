def newCust():
    Cust1 = 1 + input("Please enter")
    Cust2 = 2 + input("Please enter after previous customer")
    return Cust1,Cust2


def custConfirm(Cust1,Cust2):
    if Cust1 == 1:
        print("New customer has been added")
    elif Cust2 == 2:
        print("Second new customer has been added")
    else:
        print("Please resubmit your entry.")



