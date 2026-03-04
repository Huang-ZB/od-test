minAverageLost = int(input())
a = list(map(int,input().split()))


lo = 0
hi = 1
sum1 = a[0] + a[1]
cur_len = hi-lo+1
n = len(a)
max_len = 0
ans = []
while hi < n and lo< hi:
    ave = sum1 / (cur_len)
    # 如果在最小值以内
    if ave <= minAverageLost:
        # 判断最大长度，更大则更换；等于，则添加坐标
        if cur_len > max_len:
            max_len = cur_len
            ans = [[lo,hi]]
        elif cur_len == max_len:
            ans.append([lo,hi])
        hi += 1
        if hi < n-1:
            cur_len += 1
            sum1 += a[hi]
    else:
        # 如果超过最小值，则缩小范围
        sum1 -= a[lo]
        lo += 1
        cur_len -= 1
        # 如果指针重合
        if lo == hi and hi < n-1:
            hi += 1
            sum1 += a[hi]
            cur_len += 1


str_a = ['-'.join(map(str,i)) for i in ans]
print(' '.join(str_a))


