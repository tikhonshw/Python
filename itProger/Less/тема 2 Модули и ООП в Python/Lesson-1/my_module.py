if __name__ == "__main__":
    print("Hi")

some = 12

def printSome(str):
    print("Результат:", str)

def summ(*args):
    summa = 0
    for i in args:
        summa += i

    return summa
