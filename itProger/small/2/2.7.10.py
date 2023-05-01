'''
Создайте словарь students. В качестве ключей пропишите значения: «physics, math, biology».
В качестве значений ко всем ключам пропишите список состоящий из элементов: «Bob, Alex, Micke».
На экран сперва выведите весь словарь students, а затем лишь значение по ключу «math».
'''

students = {
    'physics': ["Bob", "Alex", "Micke"],
    'math': ["Bob", "Alex", "Micke"],
    'biology': ["Bob", "Alex", "Micke"]
}
print(students)
print(students['math'])