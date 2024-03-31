import time

print(6 + 23)
print(34 * 3)
print(46 / 6)
print(20 == 20)


A = 10
F = 15
if A < F:
    print("A is less than F")
elif A == F:
    print(" A is equal to F")
else:
    print("A is greater than F")

A = 1
while A <= 5:
    print("Good Evening!")
    A = A + 1

for s in range (15):
    print(s + 1)
    sleep.time(1.5)

Family = ['Sylvia', 'Patrick', 'Tamekia', 'Sergio', 'Ruby', 'Marion']
for item in Family:
    print(item)

person = ("Andrew", 21, "male")

print(person.count("Andrew"))
print(person.index("male"))

for x in person:
    print(x)

if "Andrew" in person:
    print("Andrew is goooone!!!")

#You can return a string number or value of the expression following the return,keyword to the caller.

name = input("Your name is?")
car = input("Car you are purchasing?")

def car_purchase(name, car):
    print("Good morning, (name) may i ask what (car)")

car_purchase(name, car)



