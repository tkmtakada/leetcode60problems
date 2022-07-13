#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # ながさ2以上であることが保証されている
        prev, cur, nex = head, head.next, head.next.next
        prev.next = None
        while nex is not None:
            # print("prev", prev)
            # print("cur", cur)
            # print("nex", nex)
            # print("==========")
            cur.next = prev
            prev, cur, nex = cur, nex, nex.next
        cur.next = prev
        return cur

# @lc code=end

