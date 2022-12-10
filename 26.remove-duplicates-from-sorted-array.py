#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[cur]:  # 問題あり
                continue  # i を進めることしかできない
            else:  # 順当
                cur += 1
                nums[cur] = nums[i]                
        print(nums)
        return cur+1
        


# @lc code=end