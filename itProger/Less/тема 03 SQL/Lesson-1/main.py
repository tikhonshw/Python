import sqlite3 as sql

# Создание файла с базой данных
conn = sql.connect('itproger.sqlite')
cur = conn.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS users (
    id int auto_increment primary key,
    name varchar(50),
    password varchar(50)
) ''')
conn.commit()

user_name = input('Введите ваше имя: ')
user_pass = input('Введите пароль: ')

cur.execute('INSERT INTO users (name, password) VALUES (\'%s\', \'%s\')'%(user_name, user_pass))
conn.commit()

print('Список пользователей:\n')
cur.execute('SELECT * FROM users')
users = cur.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Пароль: {user[2]}')

cur.close()
conn.close()
