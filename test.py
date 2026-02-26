import enum
import sys

def solve(sum_l,sum_front,up_num):
    if sum_l % 3 != 0:
        return 0
    l_store = []
    l_store2 = []
    # 找到第一段目标值 且第一段有正数
    for i, num_sum in enumerate(sum_front):
        if num_sum == sum_l//3 and up_num[i] > 0:
            l_store.append(i)
    # 找到第二段目标值 且第二段有正数
    for i,num_sum in enumerate(sum_front):
        if num_sum == 2 * sum_l //3 :
            l_store2.append(i)
    cnt = 0
    if l_store and l_store2:
        for i in l_store:
            for j in l_store2:
                # 保证二、三段都含有正数
                if up_num[j] - up_num[i] > 0 and up_num[-1] - up_num[j] > 0:
                    cnt +=1
        return cnt
    else:
        return 0

n = int(input())
l = list(map(int,input().split()))
# 前缀和
sum_front = [0] * n
sum_front[0] = l[0]
# 记录正数个数总和
up_num = [0]*n
if l[0] > 0:
    up_num[0] = 1
for i in range(1,n):
    sum_front[i] = l[i] + sum_front[i-1]
    if l[i] > 0:
        up_num[i] = 1 + up_num[i-1]
    else:
        up_num[i] = up_num[i-1]
sum_l = sum_front[-1]



print(solve(sum_l,sum_front,up_num))
