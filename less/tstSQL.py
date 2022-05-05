import mysql.connector

try:
    connection = mysql.connector.connect(host='10.152.36.10',
                                         database='arm_vdo',
                                         user='root',
                                         password='3333')

    sql_select_Query = 'SELECT concat(ob.vidTO, " ", nameOb.name) FROM arm_vdo.grafTO_planTO as ob Left JOIN arm_vdo.grafTO_oborudovanie as nameOb ON ob.idSred = nameOb.id where yearTO = 2022 and datePlanTO = "2022-04-01"'
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    # print("Total number of rows in table: ", cursor.rowcount)

    # print("\nPrinting each row")
    for row in records:
        print(row[0])
        # print("Id = ", row[0], )
        # print("Name = ", row[1])
        # print("Price  = ", row[2])
        # print("Purchase date  = ", row[3], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        # print("MySQL connection is closed")
