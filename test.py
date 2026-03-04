import sys

with open("test.txt", "r", encoding="utf-8") as f:
    sys.stdin = f
    n, t, k = [int(i) for i in input().split()]
    krl = [int(i) for i in input().split()]

# 求k个和为t的组合


# 对于每个数有选和不选的策略
def solution(n, t, k, krl, index, pre_sum, pre_quantity, result, ans):
    # 对于当前的数
    if index > n - 1:
        return
    # 不选择
    solution(n, t, k, krl, index + 1, pre_sum, pre_quantity, result, ans)

    # 选择
    cur_sum = pre_sum + krl[index]
    cur_quantity = pre_quantity + 1
    if cur_sum > t:
        return
    if cur_quantity > k:
        return
    if cur_quantity == k and cur_sum == t:
        ans.append(result + [index])
        return
    else:
        solution(n, t, k, krl, index + 1, cur_sum, cur_quantity, result + [index], ans)
    return


ans = []
result = []
pre_sum = 0
pre_quantity = 0
solution(n, t, k, krl, 0, 0, 0, result, ans)
print(len(ans))
