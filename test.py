import sys


# 等价于求，max(len1,len2)- 最长公共子序列的长度
s = input()
t = input()
if len(s) < len(t):
    s,t =t,s
n = len(s)
m = len(t)
# dp[i][j] 表示s的前i个和t的前j个公共子序列的长度
dp = [[0]*(m+1)  for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i][j-1])

print(dp[n+1][m+1])
