#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for i in range(len(s)):
            if s[i] in mp:
                mp[s[i]].append(i)
            else:
                mp[s[i]] = [i]

        for k, v in mp.items():
            if len(v) == 1:
                return v[0]
        return -1

        
# @lc code=end

