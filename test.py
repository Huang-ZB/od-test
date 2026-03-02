'''
描述
一个 V × M 的由非负整数构成的数字矩阵，你需要在其中取出若干个数字，使得取出的任意两个数字不相邻 （若一个数字在另外一个数字
相邻8个格子中的一个即认为这两个数字相邻），求取出数字和最大是多少，
输入描述：
第一行有一个正整数T （1 ≤T≤ 20），表示了有T 组数据。
对于每一组数据，第一行有两个正整数V，IM （1 ≤ V，M ≤6），表示了数字矩阵为 N行 M 列。
接下来 N 行， 每行 M 个非负整数，描述了这个数字矩阵，满足 1 ≤ aij ≤ 105。
输出描述：
输出共 T 行，每行一个非负整数，输出所求得的答案。
示例1
输入：1
复制
33
1 1 1
1 1 1
1 1 1
输出： 4
复制'''
import sys
class Solution:
    def max_sum(self,grid,n,m):
        res = []
        # 初始化起始位置
        for i in range(n):
            for j in range(m):
                visited = [[False for j in range(m)] for i in range(n)]
                start = (i,j)
                self.visited_trans(visited,start)
                self.dfs(self,grid,n,m,visited,start,res)
        
        return    

    def visited_trans(visited,node,flag = True):
        dx,dy = node
        way = ((0,0),(1,0),(0,1),(1,1),(-1,-1),(0,-1),(-1,0),(-1,1),(1,-1))
        for i in way:
            visited[node + i[0]][node + i[1]] = flag
        return

    def dfs(self,grid,n,m,visited,start,pre_sum,res):
        # 访问当前节点
        dx,dy = start
        visited[dx][dy] = True
        # 访问后还需要把周围的点也要标记为访问过了，反正走回来
        
        cur_sum = pre_sum + grid[dx][dy]
        res[0] = max(res[0],cur_sum)
        
        # 终止条件
        flag = False

        # 访问下一个节点
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                self.visited_trans(visited,(i,j),flag=False)
                self.dfs(grid,n,m,visited,(i,j),cur_sum,res)
                self.visited_trans(visited,(i,j))
                # cur_sum有点类似于path的作用，但是由于是不可变变量，就不需要回溯了
        return

    

            
            