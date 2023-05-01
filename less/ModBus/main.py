from pyModbusTCP.client import ModbusClient

# Создание объекта клиента Modbus TCP
client = ModbusClient(host="10.3.103.20", port=522)

# Открытие соединения с устройством
if client.open():
    # Чтение значений из регистров
    # В данном примере читаем 10 значений, начиная с регистра 0
    register_values = client.read_holding_registers(0, 10)

    if register_values:
        # Вывод прочитанных значений на экран
        print(register_values)
    else:
        print("Ошибка чтения значений из регистров")

    # Закрытие соединения с устройством
    client.close()
else:
    print("Ошибка подключения к устройству")
