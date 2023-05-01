import crcmod

# Исходное сообщение, для которого нужно вычислить CRC16
message = b"23"
message += b"11"
message += b"04"
message += b"43"
message += b"FF"
message += b"31"
message += b"01"

# Создание объекта CRC16
crc16 = crcmod.predefined.Crc("crc-16")

# Вычисление CRC16 для сообщения
crc16.update(message)

# Получение вычисленного значения CRC16
crc_value = crc16.crcValue

# Вывод результата
print("CRC16 для сообщения {} = {}".format(message, crc_value))
