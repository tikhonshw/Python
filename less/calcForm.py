import tkinter
from tkinter import *

root = Tk()
str = StringVar()

ent = Entry(textvariable=str)
ent.insert(0, 0)

btn1 = Button(root, text="1", bg = 'blue', fg = 'white')
btn2 = Button(root, text="2", bg = 'blue', fg = 'white')
btn3 = Button(root, text="3", bg = 'blue', fg = 'white')
btn4 = Button(root, text="4", bg = 'blue', fg = 'white')
btn5 = Button(root, text="5", bg = 'blue', fg = 'white')
btn6 = Button(root, text="6", bg = 'blue', fg = 'white')
btn7 = Button(root, text="7", bg = 'blue', fg = 'white')
btn8 = Button(root, text="8", bg = 'blue', fg = 'white')
btn9 = Button(root, text="9", bg = 'blue', fg = 'white')
btn0 = Button(root, text="0", bg = 'blue', fg = 'white')
btnPlus  = Button(root, text="+", bg = 'blue', fg = 'white')
btnMinus = Button(root, text="-", bg = 'blue', fg = 'white')
btnUmn   = Button(root, text="*", bg = 'blue', fg = 'white')
btnDel   = Button(root, text="/", bg = 'blue', fg = 'white')
btnRes   = Button(root, text="=", bg = 'blue', fg = 'white')

btn1.place(x = 0,  y = 30)
btn2.place(x = 35, y = 30)
btn3.place(x = 70, y = 30)
btn4.place(x = 0,  y = 60)
btn5.place(x = 35, y = 60)
btn6.place(x = 70, y = 60)
btn7.place(x = 0,  y = 90)
btn8.place(x = 35, y = 90)
btn9.place(x = 70, y = 90)
btn0.place(x = 35, y = 120)
btnPlus.place(x = 0, y = 120)
btnMinus.place(x = 70, y = 120)
btnUmn.place(x = 0, y = 150)
btnDel.place(x = 35, y = 150)
btnRes.place(x = 70, y = 150)

ent.place(x = 0, y=0)

def f1():
    ent.insert(END, 1)

def f2():
    ent.insert(END, 2)

def f3():
    ent.insert(END, 3)

def f4():
    ent.insert(END, 4)

def f5():
    ent.insert(END, 5)

def f6():
    ent.insert(END, 6)

def f7():
    ent.insert(END, 7)

def f8():
    ent.insert(END, 8)

def f9():
    ent.insert(END, 9)

def f0():
    calc = int( ent.get() ) * 1
    if calc == 0:
        ent.delete(0, END)
        ent.insert(END, calc)
    else:
        ent.insert(END, 0)

def plus():
    tmpPer = int( ent.get() ) * 1

def res():
    ent.insert(0, tmpPer + int( ent.get() ) )

btn1['command'] = f1
btn2['command'] = f2
btn3['command'] = f3
btn4['command'] = f4
btn5['command'] = f5
btn6['command'] = f6
btn7['command'] = f7
btn8['command'] = f8
btn9['command'] = f9
btn0['command'] = f0
btnPlus['command'] = plus
btnRes['command'] = res


root.mainloop()
