##############################
##    4001    ##     966    ##
##############################
##  01 03 00 05 00 01 940B  ##
##############################
## 10.1.2.20 ## 10.3.103.20 ##
##############################
##    '01030104000188D2'    ##
##############################

# from pyModbusTCP.client import ModbusClient
# c = ModbusClient(host="10.3.103.20", port=4001, unit_id=1, auto_open=True, auto_close=True)

# regs = c.read_holding_registers(1,10)

# if regs:
#     print(regs)
# else:
#     print("read error")

from pyModbusTCP.client import ModbusClient
# from pyModbusTCP.utils import ModbusUtils
import pyModbusTCP.utils
c = ModbusClient(host ="10.3.103.20", port = 4001, auto_open=True, auto_close=True, debug=True)
# c.read_holding_registers(0, 2)
ssss = pyModbusTCP.utils.crc16(0x2304)
print (ssss)
print ( pyModbusTCP.utils.get_bits_from_int(1001) )
# if c.open():
#     print ('Start.....')
#     print (ssss)
#     # regs_list_1 = c.read_holding_registers(0, 1)
#     # regs_list_2 = c.read_holding_registers(55, 10)
#     c.close()

# from pyModbusTCP import utils

# list_16_bits = [0x0000, 0xFFFF, 0x00FF, 0x8001]

# # show "[0, -1, 255, -32767]"
# print(utils.get_list_2comp(list_16_bits, 16))

# # show "-1"
# print(utils.get_2comp(list_16_bits[1], 16))