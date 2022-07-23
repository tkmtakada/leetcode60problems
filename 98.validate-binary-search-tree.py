#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.dfs(root, -float('inf'), float('inf'))
        
    def dfs(self, root, minV, maxV):

        if root is None:
            return True
        
        if minV >= root.val or root.val >= maxV:
            return False
        
        return self.dfs(root.left, minV, root.val) and \
            self.dfs(root.right, root.val, maxV)


# @lc code=end

