#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, elt in enumerate(nums):
            m = target - elt 
            if m in mp:
                return [mp[m], i]
            else:
                mp[elt] = i
        

        return None 
# @lc code=end

