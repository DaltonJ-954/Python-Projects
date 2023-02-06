import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3, column=2, padx=(0, 30), pady=(20, 10))

        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customText)
        self.btn.grid(row=3, column=3, padx=(0, 0), pady=(20, 10))

        self.entry = Entry(width= 190)
        self.entry.grid(row=1, column=0, columnspan=4, padx=(20,10), pady=(30, 0))

        self.lbl = tk.Label(self.master,text='Enter custom text or click the Default HTML page button')
        self.lbl.grid(row=0,column=0,padx=(0, 0),pady=(25,0),sticky=N+W)

        htmlContent = "<html>\n<body>\n<h1>" + '' + "</h1>\n</body>\n</html>"
        
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    
    def customText(self):
        input_text = self.entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + input_text + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
