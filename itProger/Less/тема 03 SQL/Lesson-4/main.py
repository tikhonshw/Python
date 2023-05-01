import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database="python-example"
)

myCur = mydb.cursor()

sql = "INSERT INTO articles (title, intro, date) VALUES(%s, %s, %s)"
articles = [
    (
        '3 статья',
        'Hello text',
        '2020-10-10'
    ),
    (
        '4 статья',
        'Hello text',
        '2020-08-12'
    ),
]

myCur.executemany(sql, articles)
mydb.commit()