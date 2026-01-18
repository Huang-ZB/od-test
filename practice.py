import sys

import sys

n = int(input())
dict1 = {}
for line in sys.stdin:
    a = line.split(" ")
    if a[0] in dict1:
        dict1[a[0]] = dict1[a[0]] + int(a[1])
    else:
        dict1[a[0]] = int(a[1])

dict1 = sorted(dict1)
for i , j in dict1.items():
    print(f"{i} {j}")