#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            num_i = nums[i]
            for j in range(i+1, len(nums)):
                if num_i + nums[j] == target:
                    return [i,j]
        # return None 
# @lc code=end

