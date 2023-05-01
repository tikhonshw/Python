'''
Ниже приведен сложный список, содержащий множество вложений. Необходимо вывести на экран запись: «Why birds are not flying all the time?».
Вам необходимо прописать логичные обращения к элементам и вывести элементы в таком порядке, чтобы образовалась одна строка.
'''

data = {
    'question': ['Why', 'are', 'not', 'all'],
    'animals': {
        'birds': [
            {'name': 'birds'}
        ],
        'others': [
            [
                {'name': 'flying'},
                {'name': 'the'},
                {'name': 'time'},
            ],
        ],
    },
    'parts': {
        'question': '?'
    }
}
why = data['question'][0]
birds = data['animals']['birds'][0]['name']
are = data['question'][1]
str_not = data['question'][2]
flying = data['animals']['others'][0][0]['name']
all = data['question'][3]
the = data['animals']['others'][0][1]['name']
time = data['animals']['others'][0][2]['name']
question = data['parts']['question']
string = why + " " + birds + " " + are + " " + str_not + " " + flying + " " + all + " " + the + " " + time + question
print(string)