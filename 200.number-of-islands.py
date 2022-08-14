#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        

        self.H, self.W = len(grid), len(grid[0])
        n_island = 0
        for i in range(self.H):
            for j in range(self.W):
                cur = grid[i][j]
                if cur == "1":
                    n_island += 1
                    self.dfs(i, j, grid)
        
        return n_island


    def dfs(self, i, j , grid):
        # 陸続きの部分を＃で塗りつぶす
        
        # 終了条件
        if i<0 or j<0 or i>=self.H or j>=self.W or grid[i][j]!="1":
            return

        grid[i][j] = "#"

        self.dfs(i+1, j, grid)
        self.dfs(i, j+1, grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j-1, grid)
        

    def numIslands2(self, grid: List[List[str]]) -> int:    
        """
        2022/07/18
        """
        # 方針
        self.H, self.W = len(grid), len(grid[0])
        counter = 0
        for i in range(self.H):
            for j in range(self.W):
                if grid[i][j] == "1":  # 未知の島
                    self.dfs(grid, i, j)
                    counter += 1
        return counter

    def dfs2(self, grid, i, j):
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

