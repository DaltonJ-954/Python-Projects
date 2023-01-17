import sqlite3

conn = sqlite3.connect('assignment.db')

# Tuple names in a string
fileList = ('information.docx','Hello.txt','myImage.png' \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_text( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                text_file TEXT)')

# For every object in the tuple, it will loop to find files ending with txt
    for i in fileList:
        if i.endswith('.txt'):

        # Each row will have a value that through the tuple that loops to find
        # a file that indicates it ends with (txt.)
            cur.execute("INSERT INTO tbl_text (text_file) VALUES (?)", \
                         ("i"))
            print(i)
            
    conn.commit()
conn.close()
