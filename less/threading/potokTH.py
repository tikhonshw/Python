import time, os
from threading import Thread
from datetime import datetime, timedelta 
import threading, time
from mysql.connector import connect, Error


addresses = [] 

connection = connect(host='10.152.36.10',
                                                 database='arm_vdo',
                                                 user='root',
                                                 password='3333')
def setIpAddress():
    sql = 'SELECT ipAddr as ip FROM arm_vdo.pinger WHERE status <> 0'
    cursor = connection.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        addresses.append(row[0])
    return addresses 

def saveTimePing(ipAddr, res, unixTime):
    # try:
    #     with connection.cursor() as cursor:
    #         cursor.execute(show_table_query)
    # except Error as e:
    #     print(e)
    # print ("saveTimePing = ", ipAddr, res)
    connection = connect(host='10.152.36.10',
                        database='arm_vdo',
                        user='root',
                        password='3333')
    myCur = connection.cursor(buffered=True)

 
    sql = 'SELECT count(*) FROM pingerTmpRes WHERE ipAddr = "'+ ipAddr +'"'
    myCur.execute(sql)
    resultSql = myCur.fetchone()
    # print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! " + str(resultSql) + str(ipAddr))
    
    if int(resultSql[0]) == 0:
        sql = 'INSERT INTO pingerTmpRes (ipAddr, res, unixTime) VALUES (%s, %s, %s)'
        myCur.execute(sql, (ipAddr, res, str(unixTime) ) )
    else:
        if res > 0:
            # получаем время последнего удачного пинга и сравниваем с временем текущего 
            # если время больше заданного интервала пинга перекладываем новую запись в 
            # журнал и производим обновление новыми данными
            # sql = 'SELECT unixTime FROM pingerTmpRes WHERE ipAddr = "'+ ipAddr +'" ORDER BY id DESC limit 1'
            # myCur.execute(sql)
            # lastTimePing = myCur.fetchone() 
            # print (str(unixTime - int(lastTimePing[0]) ) )
            # print (' >>>>>>>>>>>>>>>>>>>>> ' + str(unixTime - lastTimePing))
            # if unixTime - int(lastTimePing[0]) >= 30:
            #     #добавляем в журнал запись наличия связи
            #     sql = 'INSERT INTO pingerJurnal (ipAddr, res, unixTime, status) VALUES (%s, %s, %s, %s)'
            #     myCur.execute(sql, (ipAddr, res, str(unixTime), "1" ) )
            #     #ставим статус что связь есть
            #     sql = 'UPDATE pinger SET status = "1" WHERE ipAddr = "' + ipAddr + '" '
            #     myCur.execute(sql)
            #     sql = 'UPDATE pingerTmpRes SET res = "'+ str(res) +'", unixTime = "'+ str(unixTime) +'" WHERE ipAddr = "' + ipAddr + '" '
            #     myCur.execute(sql)
            # else:
            #     #ставим статус что связь есть
            #     sql = 'UPDATE pinger SET status = "1" WHERE ipAddr = "' + ipAddr + '" '
            #     myCur.execute(sql)
            #     sql = 'UPDATE pingerTmpRes SET res = "'+ str(res) +'", unixTime = "'+ str(unixTime) +'" WHERE ipAddr = "' + ipAddr + '" '
            #     myCur.execute(sql)
            
            #добавляем в журнал запись наличия связи
            sql = 'SELECT id, status, unixTime FROM pingerJurnal WHERE ipAddr = "'+ ipAddr +'" ORDER BY id DESC limit 1'
            myCur.execute(sql)
            lastStatusJurnal = myCur.fetchone()  
            if lastStatusJurnal is not None:
                
                if int(lastStatusJurnal[1]) == 0:
                    if unixTime - int(lastStatusJurnal[2]) >= 60 * 10: #60 секунд 10 раз - порог на срабатывание записи лога
                        print('<><><><><><><><><><><><><<< ' + str(lastStatusJurnal) + ipAddr)
                        sql = 'INSERT INTO pingerJurnal (ipAddr, res, unixTime, status) VALUES (%s, %s, %s, %s)'
                        myCur.execute(sql, (ipAddr, res, str(unixTime), "1" ) )
                        # print ('+++++++++++++++++++++++++ Отмечаем записи ЧТО пинг ПОЯВИЛСЯ: ' + ipAddr + " " + str(lastStatusJurnal[0]) )
                    else:
                        # удаляем последнюю нулевую запись если пинга отсутствовала менее 30 сек
                        sql = 'DELETE FROM pingerJurnal WHERE id = "'+ str(lastStatusJurnal[0]) +'"'
                        myCur.execute(sql)                
            else:
                pass
                # print('<><><><><><><><><><><><><<< ' + ipAddr)
            
            #ставим статус что связь есть
            sql = 'UPDATE pinger SET status = "1" WHERE ipAddr = "' + ipAddr + '" and status <> 0 '
            myCur.execute(sql)

            
            sql = 'UPDATE pingerTmpRes SET res = "'+ str(res) +'", unixTime = "'+ str(unixTime) +'" WHERE ipAddr = "' + ipAddr + '" '
            myCur.execute(sql)

        else:
            # Если пинг = 0 берем текущие данные по запросу на узел (дата, адрес) добавляем статус пинга 0 (связь отсутствует)
            # и записываем данные в журнал событий, предварительно проверяем какая запись была в журанле последней.. если статус последней записи был 0
            # то запись в базу данных не добавляем
            sql = 'SELECT count(*) FROM pingerJurnal WHERE ipAddr = "'+ ipAddr +'" ORDER BY id DESC limit 1'
            myCur.execute(sql)
            resultSql = myCur.fetchone() 
            # print("____________________________", resultSql)
            if resultSql[0] == 0: # если записи не было добавляем
                sql = 'INSERT INTO pingerJurnal (ipAddr, res, unixTime, status) VALUES (%s, %s, %s, %s)'
                myCur.execute(sql, (ipAddr, res, str(unixTime), "0" ) ) 
                #ставим статус отсутствия связи
                sql = 'UPDATE pinger SET status = "3" WHERE ipAddr = "' + ipAddr + '" '
                myCur.execute(sql)
            else:
                # Если последняя запись для данного адреса стоит статус 0 запись в БД пропускае
                # если 1 то делаем новую запись
                sql = 'SELECT status FROM pingerJurnal WHERE ipAddr = "'+ ipAddr +'" ORDER BY id DESC limit 1'
                myCur.execute(sql)
                lastStatusJurnal = myCur.fetchone()  
                if int(lastStatusJurnal[0]) == 1:
                    sql = 'INSERT INTO pingerJurnal (ipAddr, res, unixTime, status) VALUES (%s, %s, %s, %s)'
                    myCur.execute(sql, (ipAddr, res, str(unixTime), "0" ) ) 
                    #ставим статус отсутствия связи
                    sql = 'UPDATE pinger SET status = "3" WHERE ipAddr = "' + ipAddr + '" '
                    myCur.execute(sql)
                    # print ('********************** Отмечаем записи ЧТО ОПЯТЬ НЕТ пинга: ' + ipAddr + " " + str(lastStatusJurnal[0]) )
                # else:
                #     print ('===================== ПРОПУСКАЕМ  проба записи нет пинга Есть в БД: ' + ipAddr + " " + str(lastStatusJurnal[0]) )


    

    # sql = 'DELETE FROM pingerTmpRes WHERE ipAddr = "'+ ipAddr +'"'
    # myCur.execute(sql)
    
    connection.commit()  
    connection.close()

def worker(ipAddr):
     
    while True:
        # 
        dateTodaySec = datetime.now()  
        dateToday = dateTodaySec.today().strftime('%d.%m.%Y %H:%M:%S') 

        unixTime = int(time.time() ) - 60 * 5 * 60
        res = os.popen('ping -c 1 -w 2 ' + ipAddr + ' | grep time= | awk \'{ print $7}\' ').read() 
        if "time=" in res: 
            timePing = float(res.split("time=")[1]) 
            res = timePing  
        else:
            res = 0
        # if res == 0:
        #     addresses.remove(ipAddr)
        #     print ('Удалил: ' + ipAddr)
        print (str(unixTime) + ' \t ' + dateToday + ' \t ' + ipAddr + ' \t' + str(res) + " ms")
        saveTimePing(ipAddr, res, unixTime)
        # addresses = setIpAddress()
        time.sleep(5)  
    
    
    

# addresses = ["10.125.25.1", "10.125.25.14", "10.3.101.34", "10.3.101.44", "10.3.101.19", "10.3.101.77", "10.125.25.2", "10.125.25.3", "10.125.25.4", "10.125.25.5", "10.125.25.6", "10.125.25.7", "10.125.25.8", "10.125.25.9", "10.125.25.10", "10.125.25.11", "10.125.25.12", "10.125.25.13", "10.125.25.14"]
addresses = setIpAddress()

def getAddr():
    for ip in addresses:
        thread = threading.Thread(target=worker, args=(ip,))
        thread.start()


if __name__ == "__main__":
    getAddr()
        # если присоединять 'thread.join()' потоки здесь, 
        # то они будут запускаться по очереди, т.к. 
        # основной поток программы будет ждать конца
        # выполнения присоединенного потока, прежде 
        # чем запустить следующий


# получаем экземпляр основного потока
main_thread = threading.main_thread()

# объединим потоки, что бы дождаться их выполнения
for t in threading.enumerate():
    # Список 'threading.enumerate()' включает в себя основной 
    # поток и т.к. присоединение основного потока самого к себе 
    # вызывает взаимоблокировку, то его необходимо пропустить
    if t is main_thread:
        continue
    # print(f'Ожидание выполнения потока {t.name}')
    # t.join()
    

# def fPing(ipAddr):
#     while True:
#         dateToday = datetime.now()  
#         dateToday = dateToday.today().strftime('%d.%m.%Y %H:%M:%S') 
#         res = os.popen('ping -c 1 -w 2 ' + ipAddr + ' | grep time= | awk \'{ print $7}\' ').read() 
#         if "time=" in res: 
#             timePing = float(res.split("time=")[1]) 
#             res = timePing 
#         else:
#             res = 0
#         print (dateToday + ' \t ' + ipAddr + ' \t' + str(res) + " ms")

#         time.sleep(5) 

# addresses = ["10.125.25.1", "10.125.25.14", "10.3.101.34", "10.3.101.44", "10.3.101.19", "10.3.101.77", "10.125.25.2", "10.125.25.3", "10.125.25.4", "10.125.25.5", "10.125.25.6", "10.125.25.7", "10.125.25.8", "10.125.25.9", "10.125.25.10", "10.125.25.11", "10.125.25.12", "10.125.25.13", "10.125.25.14"]


# if __name__ == "__main__":
#     for ip in addresses:
#         print(ip)
#         fPingTH = Thread(target=fPing, args=(ip,))
#         fPingTH.start()
#         fPingTH.join()

    # fPing1 = Thread(target=fPing, args=('10.125.25.1',0))
    # fPing2 = Thread(target=fPing, args=('10.125.25.14',0))
    # fPing3 = Thread(target=fPing, args=('10.3.101.34',0))
    # fPing4 = Thread(target=fPing, args=('10.3.101.44',0))
    # fPing5 = Thread(target=fPing, args=('10.3.101.19',0))
    # fPing6 = Thread(target=fPing, args=('10.3.101.77',0))
    # fPing1.start()
    # fPing2.start()
    # fPing3.start()
    # fPing4.start()
    # fPing5.start()
    # fPing6.start()
    
    # fPing1.join()
    # fPing2.join()
    # fPing3.join()
    # fPing4.join()
    # fPing5.join()
    # fPing6.join() 
