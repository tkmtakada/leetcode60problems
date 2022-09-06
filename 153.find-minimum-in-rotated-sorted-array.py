#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        2022/09/05
        """
        # まあ場合分けをしていく
        # pivotが右半分と左半分、どちらにあるのかを考える
        left, right = 0, len(nums) -1
        if nums[left] < nums[right]: return nums[0]
        
        while left+1 < right:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:                
                right = mid
            else:
                left = mid
            # print(nums[left:right+1])
        return nums[right]
        # return min(nums[left], nums[right])

    def findMin2(self, nums: List[int]) -> int:

        s, e = 0, len(nums)-1

        while s < e:
            m = (s + e) // 2

            # 大小関係
            if nums[s] <= nums[m] and nums[m] < nums[e]:
                return nums[s]
            elif nums[m] < nums[e] and nums[e] < nums[s]:
                e = m
            elif nums[e] < nums[m] and nums[s] <= nums[m]:
                s = m + 1
        return nums[s]

        
# @lc code=end

