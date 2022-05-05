import tkinter
from tkinter import *

root = Tk()
str1 = StringVar()
str2 = StringVar()
str3 = StringVar()

ent1 = Entry(textvariable=str1)
ent2 = Entry(textvariable=str2)
ent3 = Entry()

btn1 = Button(root, text="Hello", bg = 'blue', fg = 'white')
btn2 = Button(root, text="Bye", bg = 'blue', fg = 'white')

label1 = Label(root, text = 'press', font = 'Arial 18')

label1.place(x = 0, y = 0)
btn1.place(x = 0, y = 30)
btn2.place(x = 0, y = 60)

ent1.place(x = 0, y=90)
ent2.place(x = 0, y=120)
ent3.place(x = 0, y=150)

ent1.insert(0, 0)
ent2.insert(0, 0)


def f1():
    # root.title(btn1['text'])
    ent3.delete(0, END)
    calc = int(str1.get()) * int(str2.get())
    ent3.insert(0, calc)
    root.title(int(str1.get()) + int( str2.get()))

def f2():
    # root.title(btn2['text'])
    root.destroy()



btn1['command'] = f1
btn2['command'] = f2

root.mainloop()
