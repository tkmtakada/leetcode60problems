#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            preorder.pop(0)  # inorder[0]と一致するはず
            return TreeNode(inorder[0])
        rootVal = preorder.pop(0)
        node = TreeNode(rootVal)
        idx = inorder.index(rootVal)
        left = inorder[:idx]
        right = inorder[idx+1:]
        node.left = self.buildTree(preorder[1:], left)
        node.right = self.buildTree(preorder[1:], right)

        return node
        
# @lc code=end

