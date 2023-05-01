# Анонимные функции

mult = lambda a, x = 23: a * x

print(mult(2))
print(mult(3, 5))

mult = lambda *args: print(args)

mult(2, "String", False)
mult(3, 5)

# Обычные функции
def func(words):
    print("Переменная:", words)
    pass

func("Привет мир!")

def summ(a = 2, b = 1, x = 0):
    res = a + b + x
    return res

result = summ(5, 2, 7)
print(result, summ(45, 2))

def printAll(*params):
    for i in params:
        print(i * 2)
    print("\n")

printAll(6, "Word", 7, 9.23)
printAll(8, 2)

def printDictionary(**args):
    for key, value in args.items():
        print("Ключ:", key, ", значение:", value)

printDictionary(long="Георгий", short="Гоша", x=8, some=True)
