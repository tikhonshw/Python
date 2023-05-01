num = int(input("Введите значение: "))
bool = False

if (num > 10 or bool) and (num == 11): # True
    print("Переменная num больше чем 10")
    if num == 50:
        print("Переменная num равна 50")
    else:
        print("Переменная больше 10, но не 50")
elif num == 9:
    print("Переменная равна 9")
elif num == 8:
    print("Переменная равна 8")
else:
    print("переменная меньше 8")

number = float(input("Введите число: "))
result = "Больше 5" if number > 5.1 else "Меньше или равно 5"
print(result)

# print("Еще что-то")
