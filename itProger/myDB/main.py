import mysql.connector

mydb = mysql.connector.connect(
    host = "",      # необходимо ввести свои данные
    port = "",      # необходимо ввести свои данные
    user = "",      # необходимо ввести свои данные
    password = "",  # необходимо ввести свои данные
    database = ""   # необходимо ввести свои данные
)
myCyr = mydb.cursor()
## Из таблицы users выберите лишь пользователя, у которого поле login равен "john".
print('\nИз таблицы users выберите лишь пользователя, у которого поле login равен "john":')
sql = "SELECT * FROM users WHERE login = 'john' "
myCyr.execute(sql)
resUsers = myCyr.fetchall()
## Перебор в цикле, так как запись может быть не одна
for resUser in resUsers:
    print(resUser)

## Из таблицы items выберите лишь те товары, которые принадлежат к категории hats.
print('\nИз таблицы items выберите лишь те товары, которые принадлежат к категории hats:')
sql = "SELECT * FROM items WHERE category = 'hats' "
myCyr.execute(sql)
resItems = myCyr.fetchall()
## Перебор в цикле, так как запись может быть не одна
for resItem in resItems:
    print(resItem)

## В таблицу orders поместите новые заказы.
# В качестве user_id указываейте id пользователя что вы выбрали из таблицы users,
# а в качестве item_id указывайте id товаров, что вы выбрали из таблицы items.

## так как у нас два разных кортежа и длинна их возможно будет заранее неизвестна
#   тогда для заполнения новой таблицы используем два цикла для обхода ранее полученных данных
# !!! ВНИМАНИЕ !!! Записи будут добавлять при каждом запуске
for resUser in resUsers:
    for resItem in resItems:
        # контроль вывода перед наполнением
        # print(resUser[0], resItem[0])
        sql = "INSERT INTO orders (user_id, item_id) VALUES(%s, %s)"
        myCyr.execute(sql, (resUser[0], resItem[0]))
        mydb.commit()

## После добавления всех значений в таблицу orders выведите на экран содержимое таблицы orders в следующем формате:
# имя - описание товара
print('\nОкончательный вывод информацмм:')
sql = '''SELECT users.login, items.title FROM orders
            JOIN users ON orders.user_id = users.id
            JOIN items ON orders.item_id = items.id'''
myCyr.execute(sql)
resOrders = myCyr.fetchall()
## Перебор в цикле, так как запись может быть не одна
print('Все заказы: \n')
for resOrder in resOrders:
    print(resOrder[0], '\t-\t', resOrder[1])