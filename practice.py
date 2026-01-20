import sys
import os

import os

def get_filenames_without_extension(directory):
    """
    获取指定文件夹中所有文件的文件名（不包括扩展名）

    :param directory: 文件夹路径
    :return: 包含文件名（不包括扩展名）的列表
    """
    filenames = []
    
    # 遍历指定文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(directory):
        print(root, dirs,files)
        for file in files:
            # 分离文件名和扩展名
            filename, _ = os.path.splitext(file)
            filenames.append(filename)
    
    return filenames

# 指定要遍历的文件夹路径
directory_path = r'C:\Users\PC\Desktop\热缩套管第二批2026.1.19\output_clean'  # 请将这里替换为你的文件夹路径

# 获取文件名（不包括扩展名）
filenames_without_extension = get_filenames_without_extension(directory_path)

max_n = max(map(lambda x:len(x),filenames_without_extension))

# 打印结果
for i in range(0,len(filenames_without_extension),4):
    row = filenames_without_extension[i:i+4]
    row = list(map(lambda x: "{x:<{max_n}s}".format(x=x, max_n=max_n), row))
    print(" ".join(row))


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
# 递推式：
# dp[i] =  假设金额为i， 遍历每个硬币并计数一个硬币
# 则剩余的金额为i-coin， 而i-coin的金额是已经在之前的
# 递推已经记录，直接引用即可。
# 最后则用将dp[i]   现变量对应的值+减去变量后对应的状态（已记录


n,m = map(int,sys.stdin.readline().strip().split())
# 对应dp[i][j]满意度
# n是预算，m是物品数量
dp = [[0 for i in range(n+1)] for j in range(m+1)]

list1 = []
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().strip().split())
    list1.append([a, b, c]) 

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