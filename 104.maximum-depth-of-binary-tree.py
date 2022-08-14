#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
        # return self.dfs2(root, 0)


    def dfs(self, root, curDepth):
        """
        rootからのfarest depthを返す
        """
        if root is None:
            return curDepth
        
        return max(self.dfs(root.left, curDepth+1), \
                    self.dfs(root.right, curDepth+1))
    
    def dfs2(self, root, curDepth):
        if root is None:
            return curDepth
                
        return max(self.dfs(root.right, curDepth+1), 
            self.dfs(root.left, curDepth+1))
# @lc code=end

