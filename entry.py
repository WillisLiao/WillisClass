from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('400x300')

entry1 = Entry(root, width = 20)
entry1.pack()

def button_command():
    text = entry1.get()
    print(text)
    return None

def openNewWindow():
    root.withdraw()
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("400x300")
    Label(newWindow, text="Please choose to add or change").pack()
    btn = Button(newWindow,
                 text = "Close",
                 command = lambda: newWindowClose(newWindow))

def newWindowClose(self):
    root.deiconify()
    self.destroy()



Button(root, text="Button", command=button_command).pack()

root.mainloop()