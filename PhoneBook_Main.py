#!/usr/bin/python
# Python Ver:    3.10.1
#
# Author:        Dalton J. Walls
#
# Purpose:       Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#                using Tkinter Parent and Child relationships.
#
# Tested OS:     This code was written and tested to work with Windows 11.

from tkinter import * 
import tkinter as tk



# Be sure to import our other modules                                                                                     
# so we can have access to them
import phonebook_gui
import phonebook_func



# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Define our master frame configuration
        self.master = master
        self.master.minsize(500,300) # (Width, Height)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.config(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("W<_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)


        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: drill50_phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascade parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional parameters for additional 
            functionality or appearances such as a border width.
        """
        self.master.config(menu=menubar, borderwidth='1')





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
