from datetime import datetime, timedelta
import mysql.connector

mybd = mysql.connector.connect (
    host="10.152.36.10",
    port="3306",
    user="root",
    password="3333",
    database="arm_vdo"
)

todayTmp = datetime.today()
todayTmp = todayTmp.strftime("%Y-%m-%d %H:%M:%S")
print(todayTmp, ":")

myCurTbot = mybd.cursor(buffered=True) 

sql = '''INSERT 
            INTO arm_vdo.sp_dlink_port_arch (ip_address, short_name, status_port, dateAdd, status_line, pingTime) 
            SELECT ip_address, short_name, status_port, dateAdd, status_line, pingTime
            FROM arm_vdo.sp_dlink_port
            WHERE status_line = 0 and dateAdd <= "''' + todayTmp + '''";'''
 
myCurTbot.execute(sql)
mybd.commit()
print(myCurTbot.rowcount, " record(s) added")

sql = '''DELETE 
            FROM arm_vdo.sp_dlink_port 
            WHERE status_line = 0 and 
                dateAdd <= "''' + todayTmp + '''";'''
 
myCurTbot.execute(sql)
mybd.commit()
print(myCurTbot.rowcount, " record(s) deleted")



mybd.close()