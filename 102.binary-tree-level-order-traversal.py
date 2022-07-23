#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []        
        queue = [root]
        while len(queue) > 0:
            ans.append([])
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.pop(0)
                ans[-1].append(node.val)
                left, right = node.left, node.right
                if left is not None:
                    queue.append(left)
                if right is not None:
                    queue.append(right)
        return ans


# @lc code=end

