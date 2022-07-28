#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        if n == 2 and k == 1: return 0
        if n == 2 and k == 2: return 1 


        k = k - 1  # change to 0 index
        d = 2 ** (n - 2)
        path = []        
        while d > 1:
            r = k // d
            q = k % d
            if r == 0:
                path.append('left')
            elif r == 1:
                path.append('right')
            # else:
            #     print("wrong here, r is ", r)
            # 更新
            k = q
            d /= 2
        if q == 0:
            path.append('left')
        elif q == 1:
            path.append('right')
        # else:
        #     print("wrong")

        print("path",path)

        digit = 0
        for d in path:
            digit = self.nextDigit(digit, d)
        return digit

    def nextDigit(self, digit, d):
        if digit == 0 and d == 'left': return 0
        if digit == 0 and d == 'right': return 1
        if digit == 1 and d == 'left': return 1
        if digit == 1 and d == 'right': return 0

# @lc code=end

