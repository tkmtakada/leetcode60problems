#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    """
    DP
    cumsum --> best time to buy stock
    の２種類ある
    """
    def maxSubArray(self, nums: List[int]) -> int:
        """
        2022/08/18
        """
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:  # 直前までが負だっただら、切り捨てて自分一人の方が、まだ大きい？と見做せるため
                dp[i] = nums[i]
        return max(dp)
            
    
                        
        
    def maxSubArray2(self, nums: List[int]) -> int:
        N = len(nums)
        cumsum = [0 for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            cumsum[i+1] = nums[i] + cumsum[i]

        maxSum = [0 for _ in range(len(nums) + 1)]
        max_sum = -float('inf')
        min_sum = 0
        for i in range(1, N+1):            
            maxSum_i = cumsum[i] - min_sum            
            max_sum = max(maxSum_i, max_sum)
            min_sum = min(min_sum, cumsum[i])            
        return max_sum

# @lc code=end

