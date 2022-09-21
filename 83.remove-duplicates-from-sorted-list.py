#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return 
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                # 3, 3, 3, 2 のように、ちゃんと異なる数字が出てくれるものもあれば
                # 3, 3 のように同じ数字でそのまま終わってしまうものもある
                start = cur
                while cur.next and cur.next.val == start.val:
                    cur = cur.next
                start.next = cur.next
            else:
                cur = cur.next
        return head
# @lc code=end

