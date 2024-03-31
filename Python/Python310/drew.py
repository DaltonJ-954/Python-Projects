person = ("Andrew", 21, "male", "6 ft 2")

print(person.count("Andrew"))
print(person.index("male"))

for x in person:
    print(x)

if "Andrew" in person:
    print("Andrew is goooone!!!")


if "6 ft 2" in person:
    print("Wow, he is a nice tall guy")
