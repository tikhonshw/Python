import mysql.connector

mybd = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database="python-example"
)

myCur = mybd.cursor()

# sql = "CREATE DATABASE `python-example`"
# sql = "SHOW DATABASES"
# sql = "CREATE TABLE users (name VARCHAR(255), age INTEGER(3))"
sql = "SHOW TABLES"
myCur.execute(sql)

for el in myCur:
    print(el)
