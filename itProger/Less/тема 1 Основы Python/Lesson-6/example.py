lis = [6, 8, "Stroka", False, 46.7, 234, 1]

i = 0
while i < len(lis):
    if i % 2 == 0:
        i += 1
        continue
    print("Значение элелемента под индексом", i, "равно:", lis[i])
    i += 1

# for item in lis:
#     print("Значение элелемента равно:", item)

for word in "Hello World":
    if word == "l":
        print("Буква l была найдена")
        break
