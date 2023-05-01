'''
При помощи циклов for выполните вывод всех элементов из списков на экран.
Каждый элемент должен быть выведен по отдельности.
'''

lis = [
    ["Some", "cool", "data"],
    [54, 6],
    [-3, 0, 5.6, 4, 33, 19]
]
for i in range(len(lis)):
    for j in lis[i]:
        print(j)

print(len(lis))


lis = [
    ["Some", "cool", "data"],
    [54, 6],
    [-3, 0, 5.6, 4, 33, 19]
]
for firstList in lis:
    for el in firstList:
        print(el)