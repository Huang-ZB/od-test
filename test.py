import sys

def transfort_bin(s):
    l1  =  s.split('.')
    s_bin = ''
    for i in l1:
        if 0<=int(i) <256:
            s_bin += f'{int(i):08b}'
        else:
            return None
    return s_bin

def and_deal(mask,ip):
    sub = ''
    for i in range(32):
        if int(mask[i]) and int(ip[i]):
            sub += "1"
        else:
            sub += "0"
    return sub
        


l = sys.stdin.read().splitlines()
for i in range(0,len(l),3):
    mask = l[i]
    ip1 = l[i+1]
    ip2 = l[i+2]
    mask_bin = transfort_bin(mask)
    if not mask_bin:
        print("1")
        continue
    ip1_bin = transfort_bin(ip1)
    if not ip1_bin:
        print("1")
        continue
    ip2_bin = transfort_bin(ip2)
    if not ip2_bin:
        print("1")
        continue
    sub_1 = and_deal(mask_bin, ip1_bin)
    sub_2 = and_deal(mask_bin, ip2_bin)
    if sub_1 == sub_2:
        print("0")
    else:
        print("2")
    continue