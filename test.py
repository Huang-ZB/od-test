
high = [int(i) for i in input().split()]

n = len(high)
hi = n-1
lo = 0

S_max = 0
index = [lo,hi]
while lo < hi -1:
    min_bian = min(high[lo],high[hi])
    S = min_bian*(hi-lo-1)
    # 剪枝
    if S < S_max:
        if high[lo] > high[hi]:
            hi -= 1
        else:
            lo += 1
        continue

        
    for i in range(lo+1,hi):
        if high[i] >= min_bian:
            S -= min_bian
        else:
            S -= high[i]
    if S >= S_max:
        S_max = S
        index = [lo,hi]
    
    if high[lo] > high[hi]:
        hi -= 1
    else:
        lo += 1


if S_max == 0:
    print(0)
else:
    print(" ".join(map(str,index)),end=":")
    print(S_max)



        




