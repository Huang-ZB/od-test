n,x = list(map(int,input().split()))
arr = list(map(int,input().split()))

if x == 0:
    print((n+1)*n//2)
else:
    pre = [0] * (n+1)
    for i in range(n):
        pre[i+1] = pre[i] + arr[i]

    left = 0
    right = 0
    total = 0
    ans = 0
    while right< n:
        win_sum = pre[right+1] - pre[left]
        if win_sum < x:
            right += 1
        else:
            ans += n-right
            left += 1
    print(ans)
        
