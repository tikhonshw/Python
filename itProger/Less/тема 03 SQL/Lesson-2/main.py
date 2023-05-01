import mysql.connector

mybd = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root"
)

print(mybd)