#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp!
        n = len(s)
        dp = [[True if i>=j else False for j in range(n)] for i in range(n)]
        ans_idx = [0,1]
        for i in range(1, n):
            foundP = False
            for j in range(n-i):
                y = j
                x = j+i
                if dp[j+1][j+i-1] and (s[x]==s[y]):
                    dp[j][j+i] = True
                    ans_idx = [y, x+1]
                # dp[j][j+i] = dp[j+1][j+i-1] and (s[x]==s[y])
        # dpの右上が
        start, end = ans_idx
        return s[start:end]
        

    def longestPalindrome2(self, s: str) -> str:
        """
        ナイーブ実装でTLE
        """

        def isPalindrom(str_arr):            
            len_arr = len(str_arr)
            if len_arr == 0:
                return False
            if len_arr == 1:
                return True

            for i in range(len_arr // 2):
                if str_arr[i] != str_arr[-(i+1)]:
                    return False
            return True


        max_len = 1
        ans = s[0]
        for i in range(len(s)):
            for len_str in range(max_len, i+2):
                if isPalindrom(s[i+1-len_str:i+1]):
                    max_len = len_str
                    ans = s[i+1-len_str:i+1]
                    # print(s[i+1-len_str:i+1])
        return ans

        
# @lc code=end

