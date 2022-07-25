#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 例外地処理
        if target < nums[0]: return 0
        elif nums[-1] < target: return len(nums)
    

        l = 0
        r = len(nums) - 1
        while l < r:
            # print("cur l, r:", l, r)
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif target < nums[m]:
                r = m
        return l

# @lc code=end

