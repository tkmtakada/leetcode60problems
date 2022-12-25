#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# あ、これ解法が天才すぎた
# https://leetcode.com/problems/copy-list-with-random-pointer/solutions/43491/a-solution-with-constant-space-complexity-o-1-and-linear-time-complexity-o-n/?orderBy=most_votes
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # ------------------
        # First round
        # Make a copy list
        # ------------------

        ans = Node(head.val)
        copy_cur = ans
        cur = head.next
        while cur != null:
            copy_cur_next = Node(cur.val)
            copy_cur.next = copy_cur_next

            # update
            copy_cur = copy_cur_next
            cur = cur.next

        # while 文を抜けた時、curはnull, 
        copy_cur.next = null


        

        # Second round
# @lc code=end

