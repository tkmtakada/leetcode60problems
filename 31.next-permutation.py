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
        cur = len(nums)-2
        if nums[cur] < nums[cur+1]:
            nums[cur], nums[cur+1] = nums[cur+1], nums[cur]
        else:
            cur -= 1
            cand = nums[cur+1:]
            # candのなかで、並べた時にnums[cur]の次に大きい要素を先頭にもってくると、
            # それが辞書順で次のものになる
            _nums = nums[cur:]
            _nums.sort()
            idx = _nums.index(nums[cur])

            # 以下は、もしもnums[cur]よりも大きい値が、左にあった場合の操作
            _nums[0], _nums[idx+1] = _nums[idx+1], _nums[0]
            _nums[1:].sort()  # これで先頭を除いてpermutateできるかな？

        cur_idx = len(nums) - 2
        cand = nums[cur_idx:]
        for cur_idx in reversed(range(len(nums)-2)):
            cand = nums[cur_idx]
            if nums[cur_idx] < max(cand):
                _nums = nums[cur:]
                _nums.sort()
                target_idx = _nums.index(nums[cur])
                _nums[0], _nums[idx+1] = _nums[idx+1], _nums[0]
                _nums[1:].sort()
                nums[cur:] = _nums
                return
            else:
                pass
        if cur_idx == 0:
            nums.sort()
            return

    def nextPermutation2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        cur = N-2

        while cur >= 0:
            
            # for i in range(cur, N):
            cands = sorted(nums[cur+1:])
            for i, cand in enumerate(cands):
                """
                最初にであうcurより大きいやつが適切なSwap対象（sortした時に、
                curの次の要素になるもの）かはわからないじゃないか、と思ったけど、
                右から順に操作しているから、今までに引っかかっていない時点で、保証されるのか。
                なるほど。
                """
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

