#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        2022/08/18
        """
        minv, maxv = float('inf'), prices[0]
        maxdif = 0
        for price in prices:
            if price < minv:
                minv = price
                maxv = -float('inf')
            elif price > maxv:
                maxv = price
                maxdif = max(maxdif, maxv-minv)
        return maxdif
        
    def maxProfit2(self, prices: List[int]) -> int:
        max_profit = 0
        min_v = float('inf')
        max_v = prices[0]
        for price in prices:
            if price < min_v:
                # max_vをリセット
                min_v = price
                max_v = price
            if price > max_v:
                max_v = price
                max_profit = max(max_profit, max_v - min_v)
        return max_profit


# @lc code=end

