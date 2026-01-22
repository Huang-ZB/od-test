import sys


def IP_legal(IP: str):
    list = IP.strip().split('.')
    if "" in list or len(list) != 4:
        return False
    for i in list:
        if int(i) < 0 or int(i) >255:
            return False
    
    return True

def yanma_legal(IP: str):
    if IP_legal(IP):
        list1 = list(map(int,IP.strip().split('.')))
        s = ''.join('{:08b}'.format(i) for i in list1)
        if s == '0'*32 or s == '1'*32:
            print(s)
            return False
        count1 = s.count('01')      
        if count1 >= 1:
            print(s)
            return False
        else:
            return True
    else:
        return False 

def IP_classfy(IP:str):
    if IP_legal(IP):
        list1 = list(map(int,IP.strip().split('.')))
        if 1 <= list1[0] <= 126:
            return "A"
        if 128 <= list1[0] <= 191:
            return "B"
        if 192 <= list1[0] <= 223:
            return "C"
        if 224 <= list1[0] <= 239:
            return "D"
        if 240 <= list1[0] <= 255:
            return "E"

def IP_privite(IP:str):
    if IP_legal(IP):
        list1 = list(map(int,IP.strip().split('.')))
        if list1[0] == 10:
            return True
        if list1[0] == 172 and 16 <= list1[1] <= 31:
            return True
        if list1[0] == 192 and list1[1] == 168:
            return True

name = ['A', 'B', 'C', 'D','E','wrong', 'privite']
dict1 = dict.fromkeys(name,0)            
readall = sys.stdin.read().splitlines()
for line in readall:

    ip, yanma = line.strip().split('~')
    if not IP_legal(ip) or not yanma_legal(yanma):
        dict1['wrong'] += 1
        
    else:
        key = IP_classfy(ip)
        dict1[key] += 1
        if IP_privite(ip):
            dict1['privite'] += 1


print(' '.join([str(i) for i in dict1.values()]))
