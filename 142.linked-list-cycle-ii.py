#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # まずは、cycle listかどうかの確認
        if not head or not head.next:
            return None

        hasCycle = False
        fast = head.next.next
        slow = head.next

        
        while fast:         
            # print(fast.val, slow.val)
            if fast == slow:
                hasCycle = True
                break

            if fast.next:
                fast = fast.next.next
            else:
                # hasCycle = False
                break

            slow = slow.next
               
        # この時点で、hasCycleは信頼できる結果が入っている
        if hasCycle:
            while head != slow:
                head = head.next
                slow = slow.next
            return head
        else:
            return None
                

# @lc code=end

