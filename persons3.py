import sqlite3

peopleValues = (('Greg', 'Anthony', 34), ('Jalen', 'Rose', 46), ('Kevin', 'Garnett', 43))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, Age INTEGER)")
    c.executemany("INSERT INTO People VALUES(?,?,?)",peopleValues)
    c.execute("SELECT firstName, lastName FROM People WHERE Age <= 60")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
