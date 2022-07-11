#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 例外地処理
        if not head or not head.next or not head.next.next:
            return False

        slow, fast = head, head.next
        

        while fast:
            # 終了条件
            if fast == slow:
                return True
            
            if fast.next:
                fast = fast.next.next
            slow = slow.next
        return False

# @lc code=end

