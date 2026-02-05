from re import I
import sys

def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        i = 3
        while i*i < n:
            if num % i ==0:
                return False
        return True

def DFS(node,visited,graph,match_odd):
    # 查找node 是否被访问过，防止形成回路无限循环
    if node not in visited:
        visited.append(node)
        # 按某种顺序查找邻接点
        for even_index in graph.get(node,[]):
            # 若不为空，即有邻接点
            # 如果邻接点没有构建匹配，则构建边
            if match_odd[even_index] != -1:
                match_odd[even_index] =  node
                return True
            # 如果邻接点有构建匹配，
            else:
                # 检查邻接点的邻接点能不能构建匹配
                # 能，递归
                if DFS(match_odd[even_index],visited,graph,match_odd):
                    match_odd[even_index] = node
            # 若为空，即没有邻接点，返回False
            return False

n = int(input())
l = list(map(int,input().split()))

odd = []
even = []

for i in l:
    if i % 2 == 0 :
        even.append(i)
    else:
        odd.append(i)
graph = {}

for i, num1 in enumerate(odd):
    for j, num2  in enumerate(even):
        if is_prime(num1 + num2):
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)


match_odd = [-1]*len(even)

for i, num_odd in enumerate(odd):
    visited = []
    DFS(num_odd,visited,graph,match_odd)

max = 0
for i in match_odd:
    if i != -1:
        max += 1


print(max)