import re
import mysql.connector
import time
 
mybd = mysql.connector.connect(
    host="10.152.36.10",
    port="3306",
    user="root",
    password="3333",
    database="arm_vdo"
)

myCur = mybd.cursor(buffered=True) 

print("#########################")
print("## ОТЧЕТ наработки ДЭС ##")
print("#########################")


# with open('01.01.2019-31.12.2022.csv', 'r') as f:
#     nums = f.read().splitlines()
# print(nums)

# file = open('01.01.2019-31.12.2022.csv', 'r')
file = open('01.01.2010-29.12.2022.csv', 'r')

i = 1
add = 0
while True:
    line = file.readline()
    if not line:
        break
    # делим строку по сиполу разделения ;
    resLine = re.split(';', line.strip())
    # делим дату для разворота и дальнейшей загрузки в базу по симполу . 
    resDate = re.split(' ', resLine[0].strip())
    resDateSplit = re.split('[.]', resDate[0].strip())
    newDate = resDateSplit[2] + '-' + resDateSplit[1] + '-' + resDateSplit[0]

    newDateForSQL = newDate + ' ' + resDate[1]
    # resDate = re.split('.', resDate[0].strip()) 
    # cur.execute('INSERT INTO dga (`date`,`obj`,`about`,`dateAdd`) VALUES ("' + newDateForSQL + '", "' + resLine[1] + '", "' + resLine[2] + '","' + time.time()  + '") ')
    # print(i, ": ", newDateForSQL, " --->  " , resLine[1], " --->  " , resLine[2])
    # sql = 'INSERT INTO dga (date, obj, about) VALUES("'+newDateForSQL+'","'+resLine[1]+'", "'+resLine[2]+'")'
    # sql = 'INSERT INTO dga (date, obj, about) VALUES (%s, "{!a}", "{!a}")' #.format(newDateForSQL,resLine[1],resLine[2])
    # sql = 'INSERT INTO dga (date, obj, about) VALUES (%s, %s, %s)'
    # myCur.execute(sql, (newDateForSQL,resLine[1],resLine[2]))
    
    sqlSelect = "SELECT count(*) FROM dga WHERE date = %s and obj = %s and about = %s "
    myCur.execute(sqlSelect, (newDateForSQL, resLine[1], resLine[2]))
    resSelect = myCur.fetchone()
    # print(resSelect[0])
    if resSelect[0] == 0:
        sql = 'INSERT INTO dga (date, obj, about) VALUES (%s, %s, %s)'
        myCur.execute(sql, (newDateForSQL,resLine[1],resLine[2]))
        add = add + 1

    i = i + 1
    # if i >= 10:
    #     print('Добавлено в базу: ', add)
    #     break

# res = myCur.fetchall()
# print(res)
# for el in res:
#     print(el)
# file.close

# from datetime 
# import datetime now = datetime.now() 
# id = 1 
# formatted_date = now.strftime('%Y-%m-%d %H:%M:%S') # Assuming you have a cursor named cursor you want to execute this query on: 
# cursor.execute('insert into table(id, date_created) values(%s, %s)', (id, formatted_date)) 


print("## Обработано строк: " + str(i) + " ##")
print("#########################")


mybd.commit()