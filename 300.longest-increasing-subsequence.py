#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    """
    N^2 でまあOK
    NlogNは、わりとむずかそう
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        2022/08/18
        """
        dp = [1 for _ in nums]        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
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

