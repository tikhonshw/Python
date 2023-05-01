# coding: utf-8
import os
import urllib.request
import mysql.connector
from datetime import datetime, timedelta

mybd = mysql.connector.connect(
    host="10.152.36.10",
    port="3306",
    user="root",
    password="3333",
    database="arm_vdo"
)

massIpDlink = {'ЛАЗ СВЯЗИ': '10.125.25.1',
               'ОРЛ-Т': '10.125.25.2',
               'ПМРЦ': '10.125.25.3',
               'БПРМ-37': '10.125.25.4',
               'КРМ-217': '10.125.25.5',
               'ГРМ-37': '10.125.25.6',
               'АРП-75': '10.125.25.7',
               'ГРМ-217': '10.125.25.8',
               'ЛККС': '10.125.25.9',
               'ОРЛ-А': '10.125.25.10',
               'Вышка-КДП': '10.125.25.11',
               'ПРЦ': '10.125.25.12',
               'РМА-РМД': '10.125.25.14'
            }


def getPing(ipAdr):
    res = os.popen('ping -c 1 -w 10 ' + ipAdr + ' | grep time= | awk \'{ print $7}\' ').read()
    if "time=" in res:
        timePing = res.split('=')
        res = timePing[1] * 1
        res = filter(str.isalnum, res)
        res = "".join(res)
        res = float(res) / 10
    else:
        res = 0
    return res


def getLineStatus(ipDlink):
    res = getPing(ipDlink)

    if res > 0:
        r = urllib.request.urlopen('http://'+ ipDlink +'/DataStore/Panel.js').readlines()
        line = r[21][18:46]
        result = (ipDlink, line.decode('utf-8'), str(res))
        return result
    else:
        res = '999'
        result = (ipDlink, '0000000000000000000000000000', res)
        return result

    # r = urllib.request.urlopen('http://'+ ipDlink +'/DataStore/Panel.js').readlines()
    # line = r[21][18:46]
    # result = (ipDlink, line.decode('utf-8'), str(res))
    # return result

for name, ip in massIpDlink.items(): #range(len(massIpDlink)):
    resultDef = getLineStatus(ip)  
    if (resultDef[2] == '999'):
        status_port = '0000000000000000000000000000'
    else: 
        status_port = resultDef[1]
    
    todayTmp = datetime.today()
    todayTmp = todayTmp.strftime("%Y-%m-%d %H:%M:%S")
    myCurTbot = mybd.cursor(buffered=True) 
    
    sql = 'INSERT INTO sp_dlink_port (ip_address, short_name, status_port, dateAdd, pingTime) VALUES (%s, %s, %s, %s, %s)'
    
    myCurTbot.execute(sql, (resultDef[0], name, status_port, todayTmp, resultDef[2]))
    # print(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text)
    mybd.commit()
    # print( name, resultDef[0], resultDef[1] ) #massIpDlink[ip])

mybd.close()
