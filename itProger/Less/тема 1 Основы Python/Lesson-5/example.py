words = {'short': 'Гоша', 'long': 'Георгий'}
print(words['long'])

list = [5, "Stroka", True, 5.23, 7] # list
# list[1] = 12
list.append("Привет")
b = [5, 8, 1, 9, 6]
list.extend(b)
list.remove(5)
list.remove(5)
list.pop(0)
b.reverse()
b.clear()
list.extend([6, 2, 9, True])
# print(b)
# print(list[::3])
print(list[::])

cor = (5, "Stroka", True, 5.23, 7)
# cor[0] = 6 # Нельзя
# print(cor[0])

mult = set(list)
print(mult)

f_mult = frozenset(list)
print(f_mult)
