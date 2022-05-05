from colorama import Fore, Back, Style

what = input(Back.GREEN + "???? (+, -, *): ")
a = float( input("First num: ") )
b = float( input("Second num: ") )

if what == "+":
    c = a + b
    print("result: " + str(c) )
elif what == "-":
    c = a - b
    print("result: " + str(c) )
elif what == "*":
    c = a * b
    print("result: " + str(c) )
else:
    print("No result")
