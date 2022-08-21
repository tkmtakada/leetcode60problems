#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        2022/08/19
        """        
        total = 0
        for i in range(1, len(prices)):
            total += max(prices[i] - prices[i-1], 0)

        return total
    def maxProfit2(self, prices: List[int]) -> int:
        total = 0
        minv = prices[0]  # float('inf')
        maxv = prices[0]
        prices.append(-float('inf'))
        for price in prices:
            if price < minv:  # minを更新
                total += maxv - minv
                minv = price
                maxv = price  # maxvを更新
            elif price > maxv:
                maxv = price
            else:  # すぐに売って、min_vを更新
                total += maxv - minv
                minv = price 
                maxv = price
        return total

# @lc code=end

