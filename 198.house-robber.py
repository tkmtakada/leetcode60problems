#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0 for _ in range(N)]
        dp[N-1] = nums[N-1]
        dp[N-2] = max(nums[N-1], nums[N-2])
        for i in reversed(range(N-2)):
            dp[i] = max(nums[i] + dp[i+2], 
                        dp[i+1])
        return dp[0]


# @lc code=end

