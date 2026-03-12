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
        

import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_len = len(s)
        t_len = len(t)
        if s_len < t_len:
            return ""
        t_dict = collections.Counter(t)
        ans = []
        min_len = float("inf")
        left = 0
        for right in range(s_len):
            char = s[right]
            # 如果right是t里面的一个字符，则对应字符计数-1
            if char in t_dict:
                t_dict[char] -= 1
                # 当前字符计数≤0时，窗口内该字符数量满足t的需要；
                if t_dict[char] <= 0:
                    # 尝试检查其他字符是否也满足
                    if any(i > 0 for i in t_dict.values()):
                        continue
                    else:
                        # 其他字符也满足时，缩小窗口，直至某个字符的计数为0；即再缩小窗口则无法满足要求的情况
                        while t_dict[s[left]] < 0 :
                            t_dict[s[left]] += 1
                            left += 1
                        # 退出条件为t_dict[s[left]] = 0
                        if min_len>right-left+1:
                            min_len = right-left+1
                            ans = [left,right]
                        t_dict[s[left]] += 1
                        left +=1
                        
        if ans:
            return s[ans[0]:ans[1]+1]
        else:
            return ''

                
print(Solution().minWindow("ADOBECODEBANC","ABC"))