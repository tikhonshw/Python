#!/home/user/.local/lib/python3.6/site-packages/
import mysql.connector
from pathlib import Path
from os import path as dirPath
from docxtpl import DocxTemplate

print(dirPath.dirname('/home/user/MySoft/Python/less/energy.py'))

import time
from datetime import date, datetime, timedelta
import os

dgaStartNagr = 0

def resolvDate(dateStr):
    return dateStr.strftime('%d.%m.%Y')
def resolvDateForSQL(dateStr):
    return dateStr.strftime('%Y-%m-%d')

today = date.today()
# today = datetime.strptime("2022-04-28", "%Y-%m-%d")
if today.weekday() != 4:
    nextFr = today + timedelta(days= 4 - today.weekday() )
else:
    nextFr = today
# print(str(today.weekday()) + ' ' + str(today) + '****' + str(nextFr))

# while d.weekday() != 4:
#     d += d.timedelta(days=1)


lastWe = nextFr - timedelta(days=3)
lastTh = nextFr - timedelta(days=1)
lastFr = nextFr - timedelta(days=6)


strOut = 'Работы в системе электроснабжения, выполняемые персоналом службы ЭРТОС:'
strOut += '\nСиловые щиты:'
strOut += '\n\tЛАЗ КДП: ' + resolvDate(lastTh)
strOut += '\n\tВышка КДП: ' + resolvDate(today)
strOut += '\nРаботы, выполняемые по регламенту технического обслуживания ДЭС (в том числе плановые запуски ДЭС):'
strOut += '\n\tHimoinsa HYW 35T5: ' + resolvDate(lastWe)

answerMess = ''
connection = mysql.connector.connect(host='10.152.36.10', database='arm_vdo', user='root', password='3333')
sql_select_Query = 'SELECT datePlanTO FROM arm_vdo.grafTO_planTO WHERE idSred = 91 and datePlanTO between "'+ resolvDateForSQL(lastFr) +'" and "'+ resolvDateForSQL(today) +'" '
# sql_select_Query = 'SELECT datePlanTO FROM arm_vdo.grafTO_planTO WHERE idSred = 91 and datePlanTO between "2022-01-20" and "2022-12-30" '
cursor = connection.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
for row in records:
    print(row[0])
    answerMess += resolvDate(row[0]) + '\n'
# print(str(answerMess))
if len(answerMess) > 0:
    strOut += '\n\tHimoinsa HYW 35T5 (под нагрузкой): ' + answerMess
    dateDgaStartNagr = answerMess
    dgaStartNagr = 1
# print('длинна: ' + str(len(answerMess)) + ' ' + dateDgaStartNagr)


pathDocx = '/home/user/MySoft/Python/less/'
doc = DocxTemplate(pathDocx + 'energyReportTemplace.docx')
if doc:
    print('Файл найден')
else:
    print('Файл не найден')
if dgaStartNagr != 1:
    context = { 'dateS':      resolvDate(lastFr),
                'datePo':     resolvDate(nextFr),
                'dateLaz':    resolvDate(lastTh),
                'dateVishka': resolvDate(nextFr),
                'dateDGA':    resolvDate(lastWe)
                }
else:
    context = {'dateS': resolvDate(lastFr),
               'datePo': resolvDate(nextFr),
               'dateLaz': resolvDate(lastTh),
               'dateVishka': resolvDate(nextFr),
               'dateDGA': resolvDate(lastWe),
               'nameOVD': "Ямальский",
               'nameOb': "КДП",
               'vid': "Himoinsa HYW 35T5 (под нагрузкой)",
               'dateDGANagr': dateDgaStartNagr,
               'vidTO': "ТО-2",
               'prichina': "График ТО"
               }
doc.render(context)
nameReport = pathDocx + str(nextFr) + '_report' + '.docx'
doc.save(nameReport)

os.system('echo "Еженедельный отчет\n'+ strOut +'" | mutt -s "Еженедельный отчет главному энергетику филиала" -e "my_hdr From: GoodJob <tixon@yamal.ans.aero>" -a ' + nameReport + '  --  kdp@yamal.ans.aero, laz_kdp@yamal.ans.aero, tixon@yamal.ans.aero') #
print(str(strOut))
os.remove(nameReport)

