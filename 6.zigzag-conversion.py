#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:        
        k = numRows - 1
        if k == 0: return s

        N = len(s)
        ans = []
        
        # 最上行
        idx = 0
        while idx < N:
            ans.append(s[idx])
            idx += 2 * k
        
        # 中間行
        for r in range(1, k):
            idx1 = r
            idx2 = 2 * k - r
            while idx2 < N:  # idx2の方が先
                ans.append(s[idx1])
                ans.append(s[idx2])
                idx1 += 2 * k
                idx2 += 2 * k
            if idx1 < N:
                ans.append(s[idx1])
        
        # 最下行
        idx = k
        while idx < N:
            ans.append(s[idx])
            idx += 2 * k
        
        return "".join(ans)
# @lc code=end

