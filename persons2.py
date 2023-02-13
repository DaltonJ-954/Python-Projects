import sqlite3


# Get personal data from user and insert into a tuple
Name = input("Enter your first name: ")
Species = input("Enter your last name: ")
IQ = input("Enter your age: ")


# Execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("UPDATE People SET firstName=? WHERE firstName=? AND lastName=?",
              ('Jason', 'Vorhees', 76))
connection.commit()
