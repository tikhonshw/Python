import subprocess
import concurrent.futures
import time, os

def ping(address):
    try:
        result = subprocess.run(["ping", "-c", "1", "-W", "1", address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        timePing = float(result.stdout.split("time=")[1].split(" ms")[0])
        return address, timePing
    except subprocess.CalledProcessError:
        return address, 0

addresses = ["10.125.25.1", "10.125.25.14", "10.3.101.34", "10.3.101.44", "10.3.101.19", "10.3.101.77", "10.125.25.2", "10.125.25.3", "10.125.25.4", "10.125.25.5", "10.125.25.6", "10.125.25.7", "10.125.25.8", "10.125.25.9", "10.125.25.10", "10.125.25.11", "10.125.25.12", "10.125.25.13", "10.125.25.14"]
ping_table = {}

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = executor.map(ping, addresses)

# for addr, time in results:
#     ping_table[addr] = time

while True:
    time.sleep(10)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(ping, addresses)
        

    for addr, timePing in results:
        ping_table[addr] = timePing
    print(ping_table)
