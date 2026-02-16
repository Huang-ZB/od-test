import sys

n = int(input())
for _ in range(n):
    s = input()
    t = input()
    new_s = []
    t_null = len(t)-1
    for i in range(len(s)-1,-1,-1):
        chs = s[i]
        if s[i] == "?" or s[i] == t[t_null]:
            t_null -= 1
            new_s.append(t[t_null])
        else:
            new_s.append(s[i])
        if t_null < 0:
            print("YES")
            length = len(new_s)
            print(s[:len(s)-length].replace("?","a") + ''.join(new_s[::-1]))
            break

    if t_null >= 0:
        print("NO")
    