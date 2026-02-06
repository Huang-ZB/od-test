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
    for even_index in graph.get(node,[]):
        if even_index:
            return False # 无法构建匹配边
        else:
            if visited[even_index] == False: # 未被访问
                visited[even_index] = True
                if match_odd[even_index] == -1: # 邻未匹配
                    match_odd[even_index] =  node 
                    return True # 能构建匹配边
                else:
                    # 如果(邻-odd),匹配边的odd节点能找到另外的even进行配对，则让当前的odd与邻匹配
                    if DFS(match_odd[even_index],isited,graph,match_odd): 
                        match_odd[even_index] =  node
                        return True
                    else:
                        return False
            else:
                continue
        


    # 三种情况，无邻、有邻但邻未匹配、有邻但邻已匹配
    # 终止条件：无邻、有邻但邻未匹配
    if graph.get(node,[]) is []:
        return False
    if 

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
# { odd:[even_index1, even_index2, even_index3 ]   }
graph = {}

for i, num1 in enumerate(odd):
    for j, num2  in enumerate(even):
        if is_prime(num1 + num2):
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)

# 标记数组表示even已与某odd进行匹配，match_odd[j]=i
# j->even_index ; i -> odd_num
match_odd = [-1]*len(even)

for i, odd_num in enumerate(odd):
    # visited 标记该次dfs的even节点是否被访问过
    visited = [False] * len(even)
    DFS(odd_num,visited,graph,match_odd)

max = 0
for i in match_odd:
    if i != -1:
        max += 1


print(max)