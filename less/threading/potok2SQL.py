import subprocess
import concurrent.futures
import time, os
import mysql.connector


addresses = [] 
connection = mysql.connector.connect(host='10.152.36.10',
                                                 database='arm_vdo',
                                                 user='root',
                                                 password='3333')
def setIpAddress():
    sql = 'SELECT ipAddr as ip FROM arm_vdo.pinger WHERE status <> 0'
    cursor = connection.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        addresses.append(row[0])
    return addresses
    connection.close()

# print(addresses)

def ping(address):
    try:
        result = subprocess.run(["ping", "-c", "1", "-W", "1", address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        timePing = float(result.stdout.split("time=")[1].split(" ms")[0])
        return address, timePing
    except subprocess.CalledProcessError:
        return address, 0

# addresses = ["10.125.25.1", "10.125.25.14", "10.3.101.34", "10.3.101.44", "10.3.101.19", "10.3.101.77", "10.125.25.2", "10.125.25.3", "10.125.25.4", "10.125.25.5", "10.125.25.6", "10.125.25.7", "10.125.25.8", "10.125.25.9", "10.125.25.10", "10.125.25.11", "10.125.25.12", "10.125.25.13", "10.125.25.14"]
ping_table = {}

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(ping, addresses)

myCur = connection.cursor(buffered=True) 
for addr, timePing in results:
    ping_table[addr] = timePing
    sql = 'INSERT INTO pingerTmpRes (ipAddr, res) VALUES (%s, %s)'
    myCur.execute(sql, (addr, timePing) )





# print(ping_table)

while True:
    
    time.sleep(5)
    addresses = setIpAddress()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(ping, addresses)
        

    # for addr, timePing in results:
    #     ping_table[addr] = timePing

    myCur = connection.cursor(buffered=True) 
    for addr, timePing in results:
        ping_table[addr] = timePing
        sql = 'DELETE FROM pingerTmpRes WHERE ipAddr = "'+ addr +'"'
        myCur.execute(sql)
        sql = 'INSERT INTO pingerTmpRes (ipAddr, res) VALUES (%s, %s)'
        myCur.execute(sql, (addr, timePing) )
    connection.commit() #connection.

    # myCur.close() #connection.
    
    print(ping_table)
