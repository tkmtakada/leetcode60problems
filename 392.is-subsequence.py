#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        mp = {}
        for i, char in enumerate(t):
            if char in mp:
                mp[char].append(i)
            else:
                mp[char] = [i]
        # print("Map is ", mp)
        idx = -1
        for char in s:
            if char in mp:
                idx_lst = mp[char]
            else:
                return False
            # ここでbinary searchすればはやいけど...   
            foundNext = False                   
            for i in idx_lst:
                if idx < i:
                    idx = i
                    foundNext = True
                    # print("index: ", i)
                    break
            if not foundNext:
                return False
        return True
# @lc code=end

