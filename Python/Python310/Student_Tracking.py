from tkinter import * 
import tkinter as tk


# import all modules in the app
import student_gui
import student_func



# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Define our master frame confirguration
        self.master = master
        self.master.minsize(600,450) # (Width, Height)
        self.master.maxsize(600,450)
        # This CenterWindow method will center our app on the user's screen
        student_func.center_window(self,600,450)
        self.master.title("The Tkinter Student Tracking")
        self.master.config(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("W<_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        student_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
