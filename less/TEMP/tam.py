age = float(input("Введите количество лет автомобиля: "))



if 3 > age >= 0:
    # print("Ваш авто младше трех лет")
    cost = float(input("Введите стоимость авто в Евро: "))
    volume = int(input("Введите объем двигателя: "))
    if cost < 8500:
        result_sbor = volume * 2.5
    elif 8500 <= cost < 16700:
        result_sbor = volume * 2.5
    else:
        result_sbor = volume * 111

    print(f'Таможенный сбор: {str(result_sbor)}')
elif age >= 3:
    print("Ваш авто страше трех лет")
else:
    print("не верно указан год")


