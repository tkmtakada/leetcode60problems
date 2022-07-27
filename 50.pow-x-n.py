#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1     
        
        # 調整
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1        
        while abs(n) > 1:
            if n % 2 == 0:
                n = n / 2
                x = x ** 2
            else:
                ans *= x
                x = x ** 2
                if n > 0:
                    n = (n - 1)/2
                else:
                    n = (n + 1)/2

        return ans * x if n > 0 else 1 / (ans * x)

# @lc code=end

