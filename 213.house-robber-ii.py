#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 同時には取れないから、nums[:-1]か、nums[1:]で
        # sumが大きい方を選べばいい。
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
            
        return max(self.simple_rob(nums[:-1]), 
                    self.simple_rob(nums[1:]))
    def simple_rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0 for _ in range(N)]
        dp[N-1] = nums[N-1]
        dp[N-2] = max(nums[N-1], nums[N-2])
        for i in reversed(range(N-2)):
            dp[i] = max(nums[i] + dp[i+2], 
                        dp[i+1])
        return dp[0]
        
# @lc code=end

