import sys
import collections
matirx = []
for line in sys.stdin.readlines():
    matirx.append(line.strip().split())


def solution(matirx):
    row = len(matirx)
    col = len(matirx[0])
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    Yes_zone = collections.deque()
    NO_count = 0
    for i in range(row):
        for j in range(col):
            if matirx[i][j] == 'YES':
                Yes_zone.append((i,j,0))
            elif matirx[i][j] == 'NO':
                NO_count += 1

    if not Yes_zone:
        return -1
    if NO_count == 0:
        return 0
    day = 0
    while Yes_zone:
        x,y,day = Yes_zone.popleft()
        for dx,dy in direction:
            nx ,ny = x+dx,y+dy
            if 0<= nx < row and  0<= ny < col:
                if matirx[nx][ny] == "NO" :
                    matirx[nx][ny] = "YES"
                    NO_count -= 1
                    Yes_zone.append((nx,ny,day + 1))

    # 循环完后，若还有NO存在，说明是在死角
    if NO_count:
        return -1
    else:
        return day

print(solution(matirx))


