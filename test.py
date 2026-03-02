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
class solution:
    def max_sum(self, result, nums):
        result = []
        
        self.dfs(nums,[],result)

        return result

    def dfs(self, nums, path, result):
        if nums:
            return
        # 记录过往的选择的数字，取最后一个数来确定后续选择范围
        if path:
            start = path[-1] + 1
        else:
            start = 0
            
        # 在剩余的数组中选择一个数
        for i in range(len(nums[visited + 1 :])):
            num = nums[i]
            visited = i
            sum_
