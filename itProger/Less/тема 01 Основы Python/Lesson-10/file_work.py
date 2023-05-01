str = input("Введите текст: ")
str += "\n"

file = open('data/text.txt', 'a')
file.write(str)
file.close()

try:
    file = open('data/text.txt', 'rt')
    print(file.read(10))
    for line in file:
        print(line)

    file.close()
except FileNotFoundError:
    print("Такой файл был не найден")
