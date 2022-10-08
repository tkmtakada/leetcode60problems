#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        cur = ans
        k = 0
        while True:
            if l1 is None and l2 is None and k == 0:
                break
            
            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
                l1 = l1.next
            
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
                l2 = l2.next
            
            sum_digits = l1_val + l2_val + k
            r = sum_digits % 10
            cur.next = ListNode(r)            
            k = sum_digits // 10

            # update
            cur = cur.next

        return ans.next
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_str = []
        head = ListNode(0, None)
        cur = head
        carry = 0
        while l1 or l2 or carry == 1:
            if l1 and l2:
                sumVal = l1.val + l2.val + carry
            elif l1 and l2 is None:
                sumVal = l1.val + carry
            elif l1 is None and l2:
                sumVal = l2.val + carry
            elif not l1 and not l2:  # carryが生きてる
                sumVal = carry
            dig = sumVal % 10
            cur.next = ListNode(dig, None)
            cur = cur.next
            carry = sumVal // 10
            # ans_str.append(dig)
            
            # 更新
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # print(ans_str)
        return head.next


# @lc code=end

