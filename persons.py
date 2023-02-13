import sqlite3


# Get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = input("Enter your age: ")


# Execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, Age INTEGER)")
    c.execute("SELECT firstName, lastName, FROM People WHERE Age <= 60")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
