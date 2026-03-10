import heapq
m,n = list(map(int,input().split(',')))


def solution(m,n):
    if 3<= m <= 10 and 3<= n <= 100:
        pass
    else:
        return -1

    arr = []
    for _ in range(m):
        points = list(map(int,input().split(',')))
        if any( i<=0 or  i > 10 for i in points):
            return -1

        arr.append(points)

    q = []
    
    for i in range(n):
        re = [0]*12
        re[-1] = i+1
        sum_point = 0
        for j in range(m):
            
            sum_point += arr[j][i]
            
            re[11-arr[j][i]] +=1
        re[0] = sum_point

        if len(q) == 3:
            heapq.heappushpop(q,re)
        else:
            heapq.heappush(q,re)
    
    ans = []
    for i in range(3):
        ans.append(heapq.heappop(q)[-1])
    return ','.join(list(map(str,ans[::-1])))

            
        
print(solution(m,n))