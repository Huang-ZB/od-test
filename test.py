import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))

    last_occurrence = {}
    l = 0
    max_len = 0
    results = []  # 存储 [start, end]（1-indexed）

    for r in range(n):
        num = arr[r]
        # 如果 num 在当前窗口 [l, r-1] 中出现过
        if num in last_occurrence and last_occurrence[num] >= l:
            # 记录当前窗口 [l, r-1] 的长度
            cur_len = r - l
            if cur_len > max_len:
                max_len = cur_len
                results = [[l + 1, r]]  # 注意：r 是下一个位置，所以子串是 [l, r-1]
            elif cur_len == max_len:
                results.append([l + 1, r])

            # 移动左指针到重复元素的右边
            l = last_occurrence[num] + 1

        last_occurrence[num] = r

    # 处理最后一个窗口 [l, n-1]
    cur_len = n - l
    if cur_len > max_len:
        max_len = cur_len
        results = [[l + 1, n]]
    elif cur_len == max_len:
        results.append([l + 1, n])

    print(len(results))
    for start, end in results:
        print(start, end)

if __name__ == "__main__":
    main()
