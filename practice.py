import sys
import os




# var1 = 'Hello World!'
# list1 = list(var1)
# list1.reverse()

# set1 = set(list1)
# for i in set1:
#     print(i,end="")
# print(list1)    

# def f(list1 : list, m : int):
#     # -1默认无法凑出
#     dp = [m+1]*(m+1)
#     # 当硬币面值=面值，则为1
#     for i in list1:
#         dp[i] = 1
#     for i in range(1,m+1):
#         for coin in list1:
#             if coin <= i:
#                 dp[i] = min(dp[i],dp[i-coin]+1)
            
#     return dp[m]

# coins = [1, 2, 5]
# amount = 11
# print(f(coins,amount))

# dp[i] 金额对于的最少硬币数
# 初始条件为，dp[coin] = 1
# 递推式:
# dp[i] =  假设金额为i， 遍历每个硬币并计数一个硬币
# 则剩余的金额为i-coin， 而i-coin的金额是已经在之前的
# 递推已经记录，直接引用即可。
# 最后则用将dp[i]   现变量对应的值+减去变量后对应的状态(已记录

# n是金额p， m是物品数量
n, m = map(int, sys.stdin.readline().strip().split())



# 记录每个物品的价格、满意度(价格*重要度）、主附件
list1 = []
for i in range(m):
    a, b, c = map(int,sys.stdin.readline().strip().split())
    p, v, q = [a, a*b, c] 
    list1.append([p, v, q]) 

# 记录主件对应的附件
list2 = []*m
for i in range(m):
    if list1[i][2] !=0:
        list2[list1[i][2]].append(i)

'''
初始化
边界确定，物品数量:0~m;容量(金额）:0~n;
求最大值，则他最基础的条件为什么都不选(对应dp[i]=0)
或者金额为0(对应dp[0]=0)
'''
# 对应dp[i]=满意度，i为金额数
dp = [[0 for i in range(n+1)] ]




# 初始条件为使用单个物品的满意度
for i in list1:
    monny = i[0]
    importent = i[1]
    myd = monny*importent
    if dp[monny][1] < myd:
        dp[monny][1] = myd

# 递推条件
for i in range(n+1):
    for j in range(m+1):
        for wuping in list1:
            if wuping[0] < i:
                dp[i][j] = max (dp[i][j], dp[i-wuping[0]+wuping[0]*wuping[1]])

print(dp[n][m])