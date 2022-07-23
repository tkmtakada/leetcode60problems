#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]

        maxLength = 1
        for i in range(1, len(nums)):
            maxLength = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLength = max(dp[j], maxLength)
            dp[i] = maxLength + 1
        print(dp)
        return max(dp)
            
            
                
# @lc code=end

