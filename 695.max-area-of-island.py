#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.H, self.W = len(grid), len(grid[0])
        
        islandId = 2  # 2start
        mp = {}
        for i in range(self.H):
            for j in range(self.W):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, islandId)
                    islandId += 1
                # 島面積の計算
                if grid[i][j] != 0:
                    # print(grid[i][j])
                    if grid[i][j] in mp:
                        mp[grid[i][j]] += 1
                    else:
                        mp[grid[i][j]] = 1
        if len(mp.values()) == 0: 
            return 0
        ans = max(mp.values())
        return ans
                

    def dfs(self, grid, i, j, islandId):
        # --- 1を#に変える ---
        # 終了条件
        if i<0 or j <0 or i>=self.H or j>=self.W or grid[i][j] != 1:
            return 
        
        grid[i][j] = islandId
        self.dfs(grid, i+1, j, islandId)
        self.dfs(grid, i, j+1, islandId)
        self.dfs(grid, i-1, j, islandId)
        self.dfs(grid, i, j-1, islandId)
# @lc code=end

