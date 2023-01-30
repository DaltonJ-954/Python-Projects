import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox



# import all modules related to this app
import student_gui
import student_main




def center_window(self, w, h): # Pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # Calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    dirCenter = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return dirCenter


# Catch if the user's clicks on the window upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to quit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)



#========================================================
def create_db(self):
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_studentClass ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            fname TEXT, \
            lname TEXT, \
            phone TEXT, \
            email TEXT, \
            current_course TEXT \
            );")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    data = ('Trish','Stratus','444-555-6666','t_stratus.com', 'biology')
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_studentClass (fname,lname,phone,email,current_course) VALUES (?,?,?,?,?)""", ('Trish','Stratus','444-555-6666','t_stratus.com', 'biology'))
            conn.commit()
    conn.close()



def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_studentClass""")
    count = cur.fetchone()[0]
    return cur,count



#Select item in Listbox
def onSelect(self,event):
    #calling the event is the self.listList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT fname,lname,phone,email,current_course FROM tbl_studentClass WHERE fname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_current_course.delete(0,END)
            self.txt_current_course.insert(0,data[4])


def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # Normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() # This will remove any blank space before and after the user's entry
    var_lname = var_lname.strip() # This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    print("Student: {} {}".format(var_fname,var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_current_course = self.txt_current_course.get().strip()
    if not "@" or not "." in var_email: # Will use this soon
        print("Incorrect email format!!!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_current_course) > 0): # Enforce the user to provide both
        conn = sqlite3.connect('student.db')
        with conn:
            cursor = conn.cursor()
            # Check the databse for existance of the fullname, if so we wil alert user and disregard request
            cursor.execute("""SELECT COUNT(fname) FROM tbl_studentClass WHERE fname = '{}'""".format(var_fname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # If this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_studentClass (fname,lname,phone,email,current_course) VALUES (?,?,?,?,?)""", (var_fname,var_lname,var_phone,var_email,var_current_course))
                self.lstList1.insert(END, var_fname) # Update listbox with the new name
                onClear(self) # Call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Errore","'{} {}' already exist in the database! Please choose a different name.".format(var_fname,var_lname))
                onClear(self) # Call all the functions to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        # Check count to ensure that this is not the last record i n 
        # the database... cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_studentClass""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted")
            if confirm:
                conn = sqlite3.connect('student.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_studentClass WHERE fname = '{}'""".format(var_select))
                onDeleted(self) # Call the functions to clear all the textboxes and the selected index of listbox
######             onRefresh(self) # update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({} {}) is the last record in the database and cannot be deleted ay this time")
    conn.close()

def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_current_course.delete(0,END)
##    onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # Clear the text in the textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_current_course.delete(0,END)


def onReFresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_studentClass""")
        count = cur.fetchone()[0]
        i = 0
        while i < count:
            cursor = conn.cursor()
            cursor.execute("""SELECT fname FROM tbl_studentClass""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # Index of the list selection
        var_value = self.lstList1.get(var_select) # List selection's text value
    except:
        messagebox.showinfo("Missing selection", "No name was selected from the listbox. \nCancelling the Update request.")
        return
    # The user will only be allowed to update changes for phone and emails.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # Normalise the data to maintain database integrity
    var_email = self.txt_email.get().strip()
    var_fname = self.txt_fname.get().strip()
    var_current_course = self.txt_current_course.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_current_course) > 0): # Ensure that there is data present
        conn = sqlite3.connect('student.db')
        with conn:
            cur = conn.cursor()
            # Count records to see th euser's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(phone) FROM tbl_studentClass WHERE phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(email) FROM tbl_studentClass WHERE email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            cur.execute("""SELECT COUNT(current_course) FROM tbl_studentClass WHERE email = '{}'""".format(var_email))
            count3 = cur.fetchone()[0]
            print(count3)
            if count == 0 or count2 == 0 or count3 == 0: # If proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request","The following changes ({}), ({}), and ({}) will be implemented for ({}). \n")
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_studentClass SET phone = '{0}', email = '{1}' WHERE fname = '{2}'""".format(var_phone,var_email,var_fname))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel Request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","For ({}), ({}), and ({}) \nalready exist in the database for this name. \nYour update request has been cancelled.".format(var_phone, var_email, var_current_course))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the from the list. \nThen edit the phone or email information.")
    onClear(self)
                


if __name__ == "__main__":
    pass
