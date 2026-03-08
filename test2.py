

import ast
import heapq
grids = ast.literal_eval(input())
lights = ast.literal_eval(input())
# grids = ast.literal_eval('[[0,1,0],[0,2,1],[0,0,0]]')
# lights = ast.literal_eval('[[1,1,3]]')

lights_dict = {(light[0],light[1]):light[2] for light in lights}

def solution(grids,lights_dict):
    # 检查地图是否为空
    if not grids:
        return -1
    # 检查起始点，终点是否为障碍物
    rown = len(grids)
    coln = len(grids[0])
    if grids[0][0] == 1 or grids[rown-1][coln-1] == 1:
        return -1
    min_grids = [[float("inf")]*coln for _ in range(rown)]
    # 起始点的等待时间
    pretime = 0
    if grids[0][0] == 2:
        pretime += lights_dict.get((0,0),0)

    min_grids[0][0] = pretime
    
    ways = [(0,1),(0,-1),(1,0),(-1,0)]
    # 处理源点
    
    pq = [(pretime,0,0)]
    
    while pq:
        # 弹出 源点到目标点耗时最短
        cur_time,cur_x,cur_y = heapq.heappop(pq)
        # 与记录的最短时间表进行比较，若时间更长说明不是最短，直接剔除
        if cur_time > min_grids[cur_x][cur_y]:
            continue
        if cur_x == rown-1 and cur_y == coln -1 :
            return cur_time
        # 查找邻接点
        for way in ways:
            dx,dy = way
            newx = cur_x + dx
            newy = cur_y + dy
            # 检查是否越界
            if  newx < 0 or newx >= rown or newy < 0 or newy >= coln:
                continue
            # 查看是否能通过
            if grids[newx][newy] == 1:
                continue
            
            # 经过时间
            througth_time = 1
            # 等待时间
            wait_time = 0
            if grids[newx][newy] == 2:
                wait_time = lights_dict.get((newx,newy),0)

            # 源点到该点的时间
            tatol_time = cur_time + througth_time + wait_time

            if tatol_time < min_grids[newx][newy]:
                min_grids[newx][newy] = tatol_time
                heapq.heappush(pq,(tatol_time,newx,newy))
    
    final_time = min_grids[rown-1][coln-1]
    return int(final_time) if final_time != float("inf") else -1
    

print(solution(grids,lights_dict))
