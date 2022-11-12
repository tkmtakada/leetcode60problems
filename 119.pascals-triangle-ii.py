#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1]
        elif rowIndex == 2:
            return [1, 1]
            
        ans = [1] * (rowIndex + 1)        
        prev = self.getRow(rowIndex-1)
        for i in range(len(prev)-1):
            ans[i+1] = prev[i] + prev[i+1]
        return ans
        
# @lc code=end

