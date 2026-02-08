import sys
import os

# 自动检测是否在本地调试（存在 test.txt 且未被 OJ 环境限制）
if __name__ == '__main__' and os.path.exists('test.txt') and 'ONLINE_JUDGE' not in os.environ:
    sys.stdin = open('test.txt', 'r')


lines = [line.strip().split() for line in sys.stdin.readlines()]
h,w = list(map(int,lines[0]))
M = []
for i in lines[1:]:
    row = list(map(int,i))
    M.append(row)
target = (h-1,w-1)

visited = set()
step = [(-1,0), (1,0), (0,1), (0,-1)]
def DFS(start, M , visited, target):   
    cur_node = None
    # 终止条件 到达目标点
    stack = [(start,[start])]
    while cur_node != target:
        cur_node,path = stack[-1]
        visited.add(cur_node)
        for way in step:
            i , j = way
            if cur_node[0]+i >= h or cur_node[0]+i < 0 or cur_node[1]+j >= w or cur_node[1]+j < 0:
                continue
            if M[cur_node[0]+i][cur_node[0]+j]  == 1:
                continue
            if M[cur_node[0]+i][cur_node[0]+j]  == 0:
                # 弹出处理的节点
                stack.pop()
                next = (cur_node[0]+i, cur_node[0]+j)
                path = path + [next]    
                stack.append((next,path))
    # cur_node == target跳出循环
    return stack[0][1]

list1 = DFS((0,0), M, visited, target)

for i in list1:
    print(i)


