import re
import operator
from collections import Counter
def main():
    print(GetIPAddresses('10.0.0.1 --- AAAABBBB.s.s.s..192.168.1.2'))
    print(GetAdminPages('admin'))
    print GetAllConnections('access_log.txt')
    print GetAdminRequests('access_log.txt')
    print GetMaximumRequests(GetAdminRequests('access_log.txt'),5)

#1
def GetIPAddresses(text):
    return re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)[0]
#2
def GetAdminPages(text):
    if re.findall('[Aa]dmin.*\.php',text):
        return True
    else:
        return False
#3
def GetAllConnections(log_file):
    dic = {}
    with open(log_file, 'r') as log:
        for line in log.readlines():
            ip = GetIPAddresses(line)
            if ip in dic:
                dic[ip] += 1
            else:
                dic[ip] = 1
    return dic

#4
def GetAdminRequests(log_file):
    all_connections = {}
    with open(log_file, 'r') as log:
        for line in log.readlines():
            if GetAdminPages(line):
                ip = GetIPAddresses(line)
                if ip in all_connections:
                    all_connections[ip] += 1
                else:
                    all_connections[ip] = 1
    return all_connections
#5
def GetMaximumRequests(connections, number):
    return sorted(connections.keys(), key=connections.get, reverse=True)[0:number]
#6
#def FindAttacker(log_file):

if __name__ == '__main__':
    main()

