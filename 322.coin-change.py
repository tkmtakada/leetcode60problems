#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        
        # 初期条件
        dp[0] = 0
        # for coin in coins:
        #     if coin <= amount:
        #     dp[coin] = 1
        
        # DPで埋めていく
        smallest = min(coins)
        for i in range(smallest, amount+1):
            minv = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    minv = min(minv, dp[i-coin])
            dp[i] = minv + 1
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

# @lc code=end

