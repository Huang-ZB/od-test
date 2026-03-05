import sys
# n为宽，m为高
n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
def check(matrix,x,y,n,m):
    ways = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
    for way in ways:
        dx,dy = way
        cnt = 1 
        cur = matrix[x][y]
        new_x = x + dx
        new_y = y + dy
        while 0<= x < n and 0<= y < m:
            # 如果与原来的相同
            if matrix[new_x][new_y] == cur:
                cnt += 1
                if cnt == 4:
                    return True
                new_x += dx 
                new_y += dy
            else:
                # 如果出现不同 更换提前退出循环
                break
    return False



def solution(arr,n,m):
    matrix = [[0]*m for col in range(n)]
    color = ["NULL",'red','blue']
    for i in range(len(arr)):
        # 红色为1，蓝色为2 
        flag = 1 if i % 2 == 0 else 2 
        # 步数
        bushu = i + 1
        # 列数
        col = arr[i] - 1
        if 0<= col < n:
            col_m = matrix[col]
            col_len = len(col_m)
            row = 0
            # 找落子点
            while col_m[row] != 0 and row < col_len:
                row +=1
            if row <col_len:
                # 没越界说明在范围里面
                col_m[row] = flag 
                if check(matrix,col,row,n,m):

                    return f'{bushu},{color[matrix[col][row]]}'
            else:
                return f'{bushu},error'
        else:
            # 列数不再范围里面
            return f"{bushu},error"


print(solution(arr,n,m))