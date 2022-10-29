#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # --- left ---
        max_left = 0        
        max_left_arr = [0 for _ in range(len(height))]
        for i in range(len(height)):
            if height[i] > max_left:
                max_left = height[i]
            max_left_arr[i] = max_left

        # --- right ---
        max_right = 0        
        max_right_arr = [0 for _ in range(len(height))]
        for j in range(1, len(height)+1):
            if height[-j] > max_right:
                max_right = height[-j]
            max_right_arr[-j] = max_right

        # --- compute trappable amount of water
        total = 0
        for k in range(len(height)):
            total += min(max_left_arr[k], max_right_arr[k]) - height[k]
        return total
                
# @lc code=end

