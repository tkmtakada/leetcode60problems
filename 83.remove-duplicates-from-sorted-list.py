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
        if head is None or head.next is None:
            return head
        cur = head

        while cur is not None and cur.next is not None:
            prev = cur
            cur = cur.next
            # 進めた後で判定
            if prev.val == cur.val:
                # curを進める
                dup_val = cur.val
                while cur.next is not None and cur.next.val == dup_val:
                    cur = cur.next
                # While文を抜けた時は、cur.nextがNoneか、Cur.nextが異なる数字になった時。
                cur = cur.next
                prev.next = cur
                # print("cur", cur)
                # print("prev", prev)
        return head

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

