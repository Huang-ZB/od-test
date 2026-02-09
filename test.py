import sys
import os


if __name__ == '__main__' and os.path.exists('test.txt') and 'ONLINE_JUDGE' not in os.environ:
    sys.stdin = open('test.txt', 'r')

def find_0(M):
    for i in range(9):
        for j in range(9):
            if M[i][j] == 0:
                return (i,j)    
    
def chech_M(M):
    for i in range(9):
        row = M[i]
        row = set(row)
        if len(row) < 9:
            return False # 存在重复
    for j in range(9):
        col = [row[j] for row in M]
        col = set(col)
        if len(col) < 9:
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            small_M = M[i][j:j+3] + M[i+1][j:j+3] + M[i+2][j:j+3]
            small_M = set(small_M)
            if len(small_M) < 9 :
                return False
    return True

def DFS(start_node_index, graph, visted, path):
    # 该题的DFS实际是一个无根节点的多叉树
    # 初始化 标记访问 并为该节点选择一个数字
    visited.add(start_node_index)
    for i in range(1,10):
        path.append(i) # 为该层添加一个决策

        # 遍历下一个层
        next_node_index = start_node_index +1
        if next_node_index != len(zero_node_graph):
            # 如果还有空没填
            DFS(next_node_index,graph, visted, path)
        else:
            # 如果== 说明已经遍历完
            for i in range(len(zero_node_graph)):
                di , dj = zero_node_graph[i]
                M[di][dj] = path[i]
            if chech_M(M):
                return M
                break
            else:
                path.pop()
    return None

M = [list(map(int, line.strip().split())) for line in sys.stdin.readlines()]

legal = [i for i in range(1,10)]

zero_node_graph = []
for i in range(9):
    for j in range(9):
        if M[i][j] == 0:
            zero_node_graph.append((i,j))
path = []
visited = set()
new_M = DFS(0, zero_node_graph,visited,path)
print(new_M)



# # 检查每行没有被填入的数字
# list_row = []
# for di in range(9):
#     row = M[di]
#     temp_set = set()
#     # 查找缺的数字
#     for i in legal:
#         if i not in row:
#             temp_set.add(i)
#     # 如果只有一个空位需要填，则弹出，并填入
#     if len(temp_set) == 1:
#         for dj in range(9):
#             if M[di][dj] ==0:
#                 m[di][dj] = temp_set.pop()
#     list_row.append(temp_set)

# list_col = []
# for dj in range(9):
#     col = [row[dj] for row in M]
#     temp_set = set()
#     # 查找缺的数字
#     for i in legal:
#         if i not in col:
#             temp_set.add(i)
#     # 如果只有一个空位需要填，则弹出，并填入
#     if len(temp_set) == 1:
#         for di in range(9):
#             if M[di][dj] ==0:
#                 m[di][dj] = temp_set.pop()
#     list_row.append(temp_set)

# for di in range(9):
#     choose1 = list_row[di]
#     for dj in range(9):
#         choose2 = list_col[dj]
        
#         for i in choose1:
#             if 

    