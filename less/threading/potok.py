import threading
import os
import time
import random

massIpDlink = {'ЛАЗ СВЯЗИ\t': '10.125.25.1',
               'ОРЛ-Т\t\t': '10.125.25.2',
               'ПМРЦ\t\t': '10.125.25.3',
               'БПРМ-37\t\t': '10.125.25.4',
               'КРМ-217\t\t': '10.125.25.5',
               'ГРМ-37\t\t': '10.125.25.6',
               'АРП-75\t\t': '10.125.25.7',
               'ГРМ-217\t\t': '10.125.25.8',
               'ЛККС\t\t': '10.125.25.9',
               'ОРЛ-А\t\t': '10.125.25.10',
               'Вышка-КДП\t': '10.125.25.11',
               'ПРЦ\t\t': '10.125.25.12',
               'РМА-РМД\t\t': '10.125.25.14'
            }

def clear():
    time.sleep(1)
    # os.system('clear')
    print('********************')
def myfunc(num):
    print('сумма: ', num * num + num / (num - 10) )

def myfunc1(a, b, c):
    print('random: ', a + b * c)


def proc(n):
    print
    "Процесс", n


p1 = threading.Thread(target=proc, name="t1", kwargs={"n": "1"})
p2 = threading.Thread(target=proc, name="t2", kwargs={"n": "2"})


while True:
    # thr1 = threading.Thread(target=myfunc, args=(1, 2)).start()
    # thr2 = threading.Thread(target=myfunc1,
    #                         args=(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))).start()
    # clear()
    # myfunc(random.randint(0, 9))
    # myfunc1(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
    # clear()
    p1.start()
    p2.start()
