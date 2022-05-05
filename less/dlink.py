import os
import urllib.request

massIp = {'Салехард - Мужи': ['10.1.2.1', '10.1.2.2', '10.1.2.20', '10.1.2.30'],
          'Салехард - Тазовский': ['192.168.116.1', '192.168.116.60']
          }

massIpDlink = ['10.125.25.1', '10.125.25.2', '10.125.25.3',
               '10.125.25.4', '10.125.25.5', '10.125.25.6',
               '10.125.25.7', '10.125.25.8', '10.125.25.9',
               '10.125.25.10', '10.125.25.11', '10.125.25.12',
               '10.125.25.14']

def getPing(ipAdr):
    res = os.popen('ping -c 1 -w 10 ' + ipAdr + ' | grep time= | awk \'{ print $7}\' ').read()
    if "time=" in res:
        timePing = res.split('=')
        res = timePing[1] * 1
        res = filter(str.isalnum, res)
        res = "".join(res)
        res = float(res) / 10
    else:
        res = 0
    return res

def getLineStatus(ipDlink):
    res = getPing(ipDlink)
    if res > 0:
        r = urllib.request.urlopen('http://'+ ipDlink +'/DataStore/Panel.js').readlines()
        line = r[21][18:46]
        return ipDlink + ' ' + str(res) + ' ' + line.decode('utf-8')
    else:
        return ipDlink + ' Host not found!!!'

for ipAdr in range(len(massIpDlink)):
    print( str(getLineStatus(massIpDlink[ipAdr])) )

for way, ipAdr  in massIp.items():
    print(way)
    for ip in ipAdr:
        print(ip + ' ' + str( getPing(ip) ) + ' ms')
