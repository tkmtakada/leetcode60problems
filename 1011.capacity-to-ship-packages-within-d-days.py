#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # sumW = sum(weights)
        s = max(weights)
        e = sum(weights)
        print("s, e: ", s, e)
        while s < e:
            m = (s + e) // 2
            if self.isLoadable(weights, days, m):
                print("Loadable with {} cap.".format(m))
                e = m
            else:
                print("Unloadable with {} cap".format(m))
                s = m + 1
        return e

    def isLoadable(self, weights, days, cap):
        total = 0
        numDays = 0
        for w in weights:
            if total + w > cap:
                total = w
                numDays += 1
            else:
                total += w
        
        if numDays < days:
            return True
        else:
            return False
# @lc code=end

