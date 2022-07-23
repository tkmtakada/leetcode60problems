#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return 
        
        ans = []
        q = [root]
        depth = 0
        while len(q) > 0:
            ans.append(deque([]))
            depth += 1
            len_q = len(q)
            for i in range(len_q):
                node = q.pop(0)
                if depth % 2 == 0:
                    ans[-1].appendleft(node.val)
                else:
                    ans[-1].append(node.val)
                left, right = node.left, node.right
                if left is not None:
                    q.append(left)
                if right is not None:
                    q.append(right)
                # if depth%2 == 0:
        return ans


# @lc code=end

