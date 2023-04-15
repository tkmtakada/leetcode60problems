#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        f(n) = (f(n-1) && nums[n-1] > 1 )
                or (f(n-2) && nums[n-2] > 2 )
                ...
        """        
        length = len(nums)
        if length <= 1: return True
        if nums[0] == 0: return False

        dp = [0] * length
        dp[0] = nums[0]

        for i in range(1, length):
            dp[i] = max(dp[i-1], i + nums[i])
            if dp[i] >= (length - 1):
                return True
            if dp[i] <= i:
                return False

        
        return False

        
# @lc code=end

