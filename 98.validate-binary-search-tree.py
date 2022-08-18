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
        """
        2022/08/18
        """
        inf = float('inf')
        return self.isValid(root.left, root.val, -inf) \
            and self.isValid(root.right, inf, root.val)

    def isValid(self, root, maxv, minv):
        # ending conditions

        if root is None:
            # 無事にNoneまで辿り着けたなら、問題なし、という感じかな？
            return True
                
        if minv < root.val and root.val < maxv: 
            # update minv, maxv 

            return self.isValid(root.left, min(maxv, root.val), minv) \
                and self.isValid(root.right, maxv, max(minv, root.val))
        else:
            return False



    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        """
        7/28
        """
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

