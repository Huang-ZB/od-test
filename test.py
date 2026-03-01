class Solution:
    def max_sum(self,grid,n,m):
        res_max = [0]
        visited = [ [False for j in range(m)] for i in range(n)]
        self.dfs()
        return res_max[0]
    def dfs(self,grid,n,m,res_max):
        # 选择一个数字
        for i in range(n):
            for j in range(m):