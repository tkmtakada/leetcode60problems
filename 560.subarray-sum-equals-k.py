#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumsum = [0]
        total = 0
        mp = {0:1}
        ans = 0
        for num in nums:
            total += num
            cumsum.append(total)
            # ここで過去の判定
            if (total - k) in mp:
                ans += mp[total - k]

            if total in mp:
                mp[total] += 1
            else:
                mp[total] = 1            

        return ans
                    
# @lc code=end

