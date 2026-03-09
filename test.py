
# 有一个数组，每次从里面取一个或两个的数，要求每次取出的组合相等，组合可以只有一个数
# 求最多的组合数

arr = list(map(int,input().split()))

# 本题限制在一层最多两个，复杂度降低很多
'''
思路
枚举一层所有可能的长度，最短为：单根最长；最长为：最长+第二长
排序，arr[left] + arr [right] == lenght
假设arr[left] + arr [right] > lenght   由于单调性，则无法找到与arr [right]匹配的组合
同理 arr[left]
特例：第一遍遍历的时候，arr[0] == lenght
注意：可能存在遍历后left和right指向同一根的情况，奇数的情况
有两种情况：一种每层都是两个积木合在一起；一种若干层是一个积木，即单根最长;其他是两积木
'''
# 升序

def solution(arr):
    arr.sort()
    min_len = arr[-1]
    max_len = arr[-1] + arr[-2]
    n = len(arr)
    if n == 1:
        return 1
    if n == 2 :
        if arr[0] == arr[1]:
            return 2
        else:
            return 1
    for i in range(min_len,max_len + 1):
        ans = 0
        left = 0
        right = n-1
        while right >= 0 and arr[right] == i:
            right -= 1
            ans += 1
    
        while left < right: # 结束后条件
            if arr[left] + arr[right] == i:
                ans += 1
                left += 1
                right -= 1
            else:
                break
        if left > right:
            return ans
    return -1
print(solution(arr))

    
