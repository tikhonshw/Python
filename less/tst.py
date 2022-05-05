# -*- coding: utf-8 -*-
import turtle
bob = turtle.Turtle()

n=200

for z in range(20):
    for i in range(4):
        bob.fd(n)
        bob.lt(90)
    n = n - 10


print(bob)

turtle.mainloop()
