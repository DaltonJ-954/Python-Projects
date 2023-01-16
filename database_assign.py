import sqlite3

hosp = sqlite3.connect('care.db') # Variable that calls on the newly created database

with hosp: # While loop that uses a cursor() function that connects the dDB to table
    cur = hosp.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_employees( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        job_title TEXT, \
        fname TEXT, \
        lname TEXT, \
        phone TEXT \
        )")
    hosp.commit() # Commits table to database
hosp.close() # Closes the function



hosp = sqlite3.connect('care.db') # Repeating the call to the database

with hosp: # Second time, the While is looping through the variables before it closes
    cur = hosp.cursor()
    cur.execute("INSERT INTO tbl_employees(job_title, fname, lname, phone) VALUES (?,?,?,?)", \
                ('doctor', 'jessy', 'coldson', '941-222-5673'))
    cur.execute("INSERT INTO tbl_employees(job_title, fname, lname, phone) VALUES (?,?,?,?)", \
                ('practitioner', 'maria', 'cruz', '941-123-0908'))
    cur.execute("INSERT INTO tbl_employees(job_title, fname, lname, phone) VALUES (?,?,?,?)", \
                ('nurse', 'elton', 'john', '941-454-0025'))
    cur.execute("INSERT INTO tbl_employees(job_title, fname, lname, phone) VALUES (?,?,?,?)", \
                ('doctor', 'elmer', 'fudd', '941-555-1119'))
    hosp.commit()
hosp.close()



hosp = sqlite3.connect('care.db')

with hosp:
    cur = hosp.cursor()
    cur.execute("SELECT job_title, fname, lname, phone FROM tbl_employees WHERE lname = 'fudd'")
    varStaff = cur.fetchall()
    for item in varStaff:
        msg = "Job_Title: {}\nFirst Name: {}\nLast Name: {}\nPhone: {}".format(item[0],item[1],item[2],item[3])
    print(msg) # Printing the variable string while loop
