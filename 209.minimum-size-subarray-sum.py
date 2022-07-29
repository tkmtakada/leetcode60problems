#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        total = 0
        s = 0
        minl = float('inf')
        for e in range(len(nums)):
            total += nums[e]
            # print("added, now total is ", nums[s:e+1])
            # minl = min(minl, e-s+1)
            while total >= target:  # ここをイコール含めるの大事、そうすることでwhile文にはいれて、minを更新できる
                minl = min(minl, e-s+1)
                # print("minl is ", minl, "total is ", total)
                total -= nums[s]
                s += 1
                # print("now substracted, total is ", nums[s:e+1])
            
        return minl if minl != float('inf') else 0
# @lc code=en
