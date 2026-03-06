import ast

matrix = ast.literal_eval(input())
lights = ast.literal_eval(input())
lights_dict = {}
row_n = len(matrix)
col_m = len(matrix[0])

for i in lights:
    row,col,time = i
    lights_dict[(row,col)] = time

visited = [[False]*col_m for _ in range(row_n)]
def dfs(grid,light,start,target,pretime):
    if start == target:
        return

    # deal with curnode
    visited[start[0]][start[1]] = True
    if start in lights_dict:
        curtime = pretime + lights_dict[start]
    curtime += 1

    # neibor
    way = {(1,0),(-1,0),(1,0),(1,0)}

    