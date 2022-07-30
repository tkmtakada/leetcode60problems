#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        cur = N-2

        while cur >= 0:
            
            # for i in range(cur, N):
            cands = sorted(nums[cur+1:])
            for i, cand in enumerate(cands):
                if nums[cur] < cand:
                    nums[cur], cands[i] = cands[i], nums[cur]
                    cands.sort()
                    nums[cur+1:] = cands
                    return 
            # for文を抜けたということは、candsの中に、
            # 大きなものは見つからなかったということ
            cur -= 1
        
        return nums.sort()
# @lc code=end

