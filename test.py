# Process input
n = int(input())
ac = list(map(int, input()))
at = list(map(int, input().split()))

# DP
# - 阶段：前i个气球的，染色为对应颜色排列的时间
# - 状态：气球排列 0, 1, 2, 01, 02, 10, 12, 20, 21, 012, 021, 102, 120, 201, 210
# - 空间压缩，原来是dp[n][15];dp[i] 只依赖于dp[i-1]，所以可以只用一个一维数组
# 初始化取最大值
dp = [1e10] * 15
for i in range(3): dp[i] = 0
for i in range(1, n+1):
    # 获取当前颜色和该位置的染色耗时
    color, time = ac[i-1], at[i-1]
    # cost保存不同颜色气球的使用染色时间
    cost = [time] * 3
    # 与当前颜色一样的染色时间为0
    cost[color] = 0
    # 前i个气球共3种颜色
    # 前i-1个气球可能为两种颜色，染色为与他们不同的即可；可能为三种颜色，染成与最后一个一样的即可
    if i >= 3:
        dp[9] = min(dp[3], dp[9]) + cost[2]  # 01|012 -> 012
        dp[10] = min(dp[4], dp[10]) + cost[1]  # 02|021 -> 021
        dp[11] = min(dp[5], dp[11]) + cost[2]  # 10|102 -> 102
        dp[12] = min(dp[6], dp[12]) + cost[0]  # 12|120 -> 120
        dp[13] = min(dp[7], dp[13]) + cost[1]  # 20|201 -> 201
        dp[14] = min(dp[8], dp[14]) + cost[0]  # 21|210 -> 210
    # 前i个气球只有2种颜色
    # 只有两种情况可以实现，前面i-1个气球全是一样的；前面i-1个气球有两种颜色，那只能把第i个气球染成与后面颜色相同的
    if i >= 2:
        dp[3] = min(dp[0], dp[3]) + cost[1]  # 0|01 -> 01
        dp[4] = min(dp[0], dp[4]) + cost[2]  # 0|02 -> 02
        dp[5] = min(dp[1], dp[5]) + cost[0]  # 1|10 -> 10
        dp[6] = min(dp[1], dp[6]) + cost[2]  # 1|12 -> 12
        dp[7] = min(dp[2], dp[7]) + cost[0]  # 2|20 -> 20
        dp[8] = min(dp[2], dp[8]) + cost[1]  # 2|21 -> 21
    # 前i个气球只有一种，[0...i-1] = 上一个染色耗时[0...i-2]+当前的耗时[i-1]
    dp[0] = dp[0] + cost[0]  # 0 -> 0
    dp[1] = dp[1] + cost[1]  # 1 -> 1
    dp[2] = dp[2] + cost[2]  # 2 -> 2
    

# Onput
print(min(dp)) 
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
