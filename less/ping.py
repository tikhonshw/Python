
from ping3 import ping, verbose_ping
import time, sys, os
# from tkintertable import TableCanvas, TableModel
outRes = ""
verbose_ping.EXCEPTIONS = True


# tframe = Frame(master)
# tframe.pack()
# table = TableCanvas(tframe)
# table.show()


def funcPing(ipAddr):
    return verbose_ping(ipAddr, count = 1)

ipMass = [['УДТ Бованенково','10.3.101.44'],['Терминал КДП Бованенково','10.3.101.34'],['УДТ Сеяха','10.3.101.34'],['Мужи','10.1.2.20']]
for i in ipMass: #range(0, len(ipMass) - 1):
    #print(i[1])
    # print(i[0] + " - " + str(funcPing(i[1]) ) + " - " + str(verbose_ping(i[1], count = 1) ) )
    outRes += i[0] + " - " + str(funcPing(i[1]) ) + " - " + str(verbose_ping(i[1], count = 1) ) + '\n'
sys.stderr.write(outRes)
sys.stdout.flush()
outRes =""
time.sleep(0.5)
# sys.stdout.flush()

while True:
    try:
        try:
            ipMass = [['УДТ Бованенково','10.3.101.44'],['Терминал КДП Бованенково','10.3.101.34'],['УДТ Сеяха','10.3.101.34'],['Мужи','10.1.2.20']]
            for i in ipMass: #range(0, len(ipMass) - 1):
                #print(i[1])
                # print(i[0] + " - " + str(funcPing(i[1]) ) + " - " + str(verbose_ping(i[1], count = 1) ) )
                outRes += i[0] + " - " + str(funcPing(i[1]) ) + " - " + str(verbose_ping(i[1], count = 1) ) + '\n'
            sys.stderr.write(outRes)
            sys.stdout.flush()
            outRes =""
            time.sleep(0.5)
        except verbose_ping.errors.HostUnknown:  # Specific error is catched.
            print("Host unknown error raised.")
        except verbose_ping.errors.PingError:  # All ping3 errors are subclasses of `PingError`.
            print("A ping error raised.")
        # time.sleep(5)
    except Exception as e:
        # logger.error(e)  # или просто print(e) если у вас логгера нет,
        print(e)
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
