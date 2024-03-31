from tkinter import *


name = 'youtube'
print(name + ' rocks!')



from tkinter import *
win = Tk()
b1 = Button(win, text="Uno")
b1.pack(side=TOP)
b1.pack(side = TOP, pady = 30)
def but1():
    print("Hey don't push my buttons!")
    b1.configure(command=but1)


