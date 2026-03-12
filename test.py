N,end = list(map(int,input().split()))
start  = 0
H = 0
ans = 0
for _ in range(N):
    x,h = list(map(int,input().split()))
    ans += (x - start)*abs(H)
    H += h
    start = x

if start <= end:
    ans += (end - start)*H 
print(ans)