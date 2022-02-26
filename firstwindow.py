from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('400x300')



def openNewWindow():
    root.withdraw()
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("400x300")
    Label(newWindow, text="This is the new window").pack()
    btn = Button(newWindow,
                 text = "Close",
                 command = lambda: newWindowClose(newWindow))
    btn.pack(pady = 5)
def newWindowClose(self):
    root.deiconify()
    self.destroy()

lab1 = Label(root, text="What do you want?")
lab1.pack(pady = 10)
btn = Button(root,
             text="Click to open a new window",
             command = openNewWindow)
btn.pack(pady = 10)

root.mainloop()

