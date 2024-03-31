print("Percentage Calculator")
print("")

x = float(input("Your Marks = "))

per = 100

y = float(input("Total Marks = "))
z = x *  per / y

print("You Got = %.2f" %z)

if z >= 355:
    print("Congratulations!")
else:
    print("Better Luck Next Time!")
