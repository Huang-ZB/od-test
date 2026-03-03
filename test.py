
import math
n = int(input())

high = []
low = {}

for _ in range(n):
    id,num,pri,pr = map(int,input().split())

    if pr == 0:
        if pri > 100:
            high.append([id,num,pri])
            continue
        else:
            if id in low:
                low[id]["num"] += num
            else:
                low[id] = {
                    "num" : num,
                    "pri" : pri
                    }   

    
for key,val in low.items():
    num,pri = val["num"],val["pri"]
    if pri < 100 and num >= 100:
        ans.append([key,num,math.ceil(pri*0.9)])

for i in sorted(ans,key = lambda x : (x[0],-x[1])):
    print(" ".join(map(str,i)))


     



