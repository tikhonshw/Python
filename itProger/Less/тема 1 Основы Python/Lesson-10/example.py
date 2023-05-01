user_input_a = False

while user_input_a == False:
    try:
        a = int(input("Введите 1 значение: "))
        user_input_a = True
    except ValueError:
        print("Введите все же число!")

user_input_b = False

while user_input_b == False:
    try:
        b = int(input("Введите 2 значение: "))
        user_input_b = True
    except ValueError:
        print("Введите все же число!")

print("Результат:", a + b)
