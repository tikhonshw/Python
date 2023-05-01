


##### MySQL
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host = "10.152.36.10",
#     port = "3306",
#     user = "root",
#     password = "3333",
#     database = "python"
# )
# print(mydb)

# myCyr = mydb.cursor()
# sql = "CREATE DATABASE python"
# sql = "SHOW DATABASEs"
# sql = 'CREATE TABLE users (name VARCHAR(30), age INT(3))'
# sql = "SHOW TABLES"

# sql = "INSERT INTO articles (title, intro, date) VALUES(%s, %s, %s)"
# article = [
#     (
#         'Вторая статья',
#         'Hello text',
#         '2020-11-12'
#     ),
#     (
#         'Вторая статья',
#         'Hello text',
#         '2020-11-12'
#     )
#
# ]
# # myCyr.execute(sql, article)
# myCyr.executemany(sql, article)
#mydb.commit()
# for el in myCyr:
#     print(el)

# sql = 'SELECT * FROM articles'
# myCyr.execute(sql)
# res = myCyr.fetchall()
# # res = myCyr.fetchone()
# for el in res:
#     print(el)

# sql = "UPDATE articles SET title = %s WHERE id = %s "
# myCyr.execute(sql, ('Updated text', 3))
# mydb.commit()

# sql = "DELETE FROM articles WHERE title = %s "
# myCyr.execute(sql, ('Updated text', ))
# mydb.commit()