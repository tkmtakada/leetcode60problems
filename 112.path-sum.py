#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        return self.dfs(root, targetSum)
        
    def dfs(self, root, targetSum):
        if root is None:
            if targetSum == 0:
                return True
            else: return False

        return self.dfs(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

    
# @lc code=end

