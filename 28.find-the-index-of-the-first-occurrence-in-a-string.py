#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # とりあえず一番簡単なものから
        len_needle = len(needle)
        len_haystack = len(haystack)
        if needle == haystack:  # 全く同じ場合
            return 0

        for i in range(len_haystack-len_needle+1):
            if haystack[i:i+len_needle] == needle:
                return i
        
        return -1
# @lc code=end

