##############################
##    4001    ##     966    ##
##############################
##  01 03 00 05 00 01 940B  ##
##############################
## 10.1.2.20 ## 10.3.103.20 ##
##############################

# coding=utf8


# coding=utf8
from pyModbusTCP.client import ModbusClient
import time
import sys

ip_address = '10.1.2.20'
c = ModbusClient()
if not c.host(ip_address):
    print("host error")
if not c.port(4001):
    print("port error")
else:
    print('port .... connection`s')
    c.open()
rr = c.read_coils(0, 1)
print(rr)
# if not rr.bits[0] and rr.bits[1]:
#     print('work')
#     sys.exit(0)
# elif rr.bits[0] and rr.bits[1]:
#     print('not work')
#     sys.exit(1)
# print('-')
sys.exit(-1)


# def main():
#     ip_address='10.1.2.20'
#     c = ModbusClient()
#     if not c.host(ip_address):
#         print("host error")
#     if not c.port(4001):
#         print("port error")
#     while True:
#         if c.is_open():
#             rr = c.read_discrete_inputs(0, 2)
#             # [False, True]
#             if not rr[0] and rr[1]:
#                 print('work')
#                 sys.exit(0)
#             # [True, True]
#             elif rr[0] and rr[1]:
#                 print ('not work')
#                 sys.exit(1)
#             print ('-')
#             sys.exit(-1)
#         else:
#             c.open()
#
# if __name__ == "__main__":
#     main()

# import modbus_tk.modbus_tcp as mt
# import modbus_tk.defines as md
#
# # Удаленно подключиться к серверу
# master = mt.TcpMaster("10.1.2.20", 40001)
# master.set_timeout(1.0)
#
#  # @ slave = 1: идентификатор ведомого от 1 до 247. 0 для трансляции всех ведомых
#  # @ function_code = READ_HOLDING_REGISTERS: коды функций
#  # @ начальный_адрес = 1: начальный адрес
#  # @ amount_of_x = 3: Количество регистров / катушек
#  # @output_value: целое или итеративное значение: 1 / [1,1,1,0,0,1] / xrange (12)
# # @data_format
# # @expected_length
# Hold_value = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=1, quantity_of_x=3, output_value=5)
# # Hold_value = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=1, quantity_of_x=3, output_value=5)
# # Coils_value = master.execute(slave=1, function_code=md.READ_COILS, starting_address=1,  quantity_of_x=3, output_value=5)
# #
# print (Hold_value) # Формат значения полученного регистра - кортеж (55, 12, 44)
# # print (Hold_value) # Формат значения выбранного регистра - кортеж (1, 1, 1)


#! /usr/bin/env python
# coding=utf-8
# import modbus_tk
# import modbus_tk.defines as cst
# import modbus_tk.modbus_tcp as modbus_tcp
# slaveIP = '10.3.103.20'
# slavePort = 4001
# master = modbus_tcp.TcpMaster(host=slaveIP, port=int(slavePort))
# master.set_timeout(0.5)
# getDi=master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 10)
# print(getDi)


# import crcmod
# str_b = bytes.fromhex('010300050001940B')
# crc16 = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True,  xorOut=0x0000)
# crc_int=crc16(str_b)
# crc_str=hex(crc_int)
# print(crc_str)

# from pymodbus.client.sync import ModbusTcpClient
# import time
# UNIT = 0x1
# client = ModbusTcpClient('10.3.103.20', port = 4001, timeout = 0.3)
# while True:
#     result = client.read_holding_registers(0, 4)
#     result = request.registers
#     print(result.bits[0])
#     print(result)
#     print(result[0])
#     time.sleep(1)
# client.close()



# from pyModbusTCP.client import ModbusClient
# c  =  ModbusClient ( host = "10.1.2.20", port = 4001, unit_id=1, auto_open = True, auto_close = True )
# regs = c.read_holding_registers(1, 4)
# if regs:
#     print(regs)
# else:
#     print("read error")

# import os
# hostname = "10.1.2.20" #example
# response = os.system("ping -c 1 " + hostname)
#
# #and then check the response...
# if response == 0:
#     print(hostname, 'is up!')
# else:
#     print(hostname, 'is down!')

# import threading
# import sys
# import time
#
#
# def thread_job(number):
#     time.sleep(2)  # "усыпляем" поток на 2 сек
#     print('Hello {}'.format(number))
#     sys.stdout.flush()
#
#
# def run_threads(count):
#     threads = [
#         threading.Thread(target=thread_job, args=(i,))
#         for i in range(1, count)
#     ]
#     for thread in threads:
#         thread.start()  # каждый поток должен быть запущен
#
#
# run_threads(6)
# print("finish")
