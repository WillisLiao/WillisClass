from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('400x300')

L1 = Label(root, text="name\nID\nheight\nweight\ngender\nemail\nphone")
L1.pack()
entry1 = Entry(root, width = 20)
entry1.pack()

entry2 = Entry(root, width = 20)
entry2.pack()

entry3 = Entry(root, width = 20)
entry3.pack()

entry4 = Entry(root, width = 20)
entry4.pack()

entry5 = Entry(root, width = 20)
entry5.pack()

entry6 = Entry(root, width = 20)
entry6.pack()

entry7 = Entry(root, width = 20)
entry7.pack()

def button_command():
    text = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    text4 = entry4.get()
    text5 = entry5.get()
    text6 = entry6.get()
    text7 = entry7.get()
    print(text)
    return None
Button(root, text="Add", command=button_command).pack()

root.mainloop()