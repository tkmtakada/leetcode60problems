#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 方針
        self.H, self.W = len(grid), len(grid[0])
        counter = 0
        for i in range(self.H):
            for j in range(self.W):
                if grid[i][j] == "1":  # 未知の島
                    self.dfs(grid, i, j)
                    counter += 1
        return counter

    def dfs(self, grid, i, j):
        # --- 1を#に変える ---
        # 終了条件
        if i<0 or j <0 or i>=self.H or j>=self.W or grid[i][j] != "1":
            return 
        
        grid[i][j] = "#"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)

# @lc code=end

