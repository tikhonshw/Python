import time, os
from threading import Thread
from datetime import datetime, timedelta
# from ping3 import ping, verbose_ping
# verbose_ping.EXCEPTIONS = True
# stop = False
def fPing(ipAddr,p):
    while True:
        dateToday = datetime.now()  
        dateToday = dateToday.today().strftime('%d.%m.%Y %H:%M:%S')
        # print(p1 ** p2)
        # print (ipAddr + ': ' + verbose_ping(ipAddr, count = 1) )
        res = os.popen('ping -c 1 -w 2 ' + ipAddr + ' | grep time= | awk \'{ print $7}\' ').read()
        #         result = subprocess.run(["ping", "-c", "1", "-W", "2", address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        #         time = float(result.stdout.split("time=")[1].split(" ms")[0])
        # ping -c 1 -w 2 10.125.25.1 | grep time= | awk \'{ print $7}\'  
        if "time=" in res:
            # timePing = float(res.split("time=")[1].split(" ms")[0])
            timePing = float(res.split("time=")[1]) 
            res = timePing
            # timePing = res.split('=')
            # res = timePing[1] * 1
            # res = filter(str.isalnum, timePing[1])
            # res = "".join(res)
            # res = float(res) / 1
        else:
            res = 0
        print (dateToday + ' \t ' + ipAddr + ' \t' + str(res) + " ms")

        time.sleep(10)
        # print('______________________________________')

if __name__ == "__main__":
    fPing1 = Thread(target=fPing, args=('10.125.25.1',0))
    fPing2 = Thread(target=fPing, args=('10.125.25.14',0))
    fPing3 = Thread(target=fPing, args=('10.3.101.34',0))
    fPing4 = Thread(target=fPing, args=('10.3.101.44',0))
    fPing5 = Thread(target=fPing, args=('10.3.101.19',0))
    fPing6 = Thread(target=fPing, args=('10.3.101.77',0))
    fPing1.start()
    fPing2.start()
    fPing3.start()
    fPing4.start()
    fPing5.start()
    fPing6.start()
    
    fPing1.join()
    fPing2.join()
    fPing3.join()
    fPing4.join()
    fPing5.join()
    fPing6.join()
    # time.sleep(2)
    # stop = True









            # import subprocess
            # import concurrent.futures

            # def ping(address):
            #     try:
            #         result = subprocess.run(["ping", "-c", "1", "-W", "2", address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            #         time = float(result.stdout.split("time=")[1].split(" ms")[0])
            #         return address, time
            #     except subprocess.CalledProcessError:
            #         return address, None

            # addresses = ["8.8.8.8", "8.8.4.4", "208.67.222.222", "208.67.220.220", "10.3.101.77"]
            # ping_table = {}

            # with concurrent.futures.ThreadPoolExecutor() as executor:
            #     results = executor.map(ping, addresses)

            # for addr, time in results:
            #     ping_table[addr] = time

            # print(ping_table)







# # from time import sleep, perf_counter
# # from threading import Thread


# # def task(p1, p2):
# #     print('Начинаем выполнение задачи...')
# #     print( p1 * p2)
# #     print('Выполнено')


# # start_time = perf_counter()

# # # создаем два новых потока
# # t1 = Thread(target=task, args = (10, 20))
# # t2 = Thread(target=task, args = (50, 40))


# # while True:
# #     sleep(1)

# #     # запускаем потоки
# #     t1.start()
# #     t2.start()

# #     # ждем, когда потоки выполнятся
# #     t1.join()
# #     t2.join()

# #     end_time = perf_counter()

# #     print(f'Выполнение заняло {end_time- start_time: 0.2f} секунд.')
