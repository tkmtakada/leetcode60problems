#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(2N)でやれば簡単かな,,,>?
        curIndex = 0
        cur = head
        while cur is not None:
            cur = cur.next
            curIndex += 1
        length = curIndex
        
        # これ、場合分けが必要だわ、
        targetIdx = length - n  # zero-indexed
        
        # ====================
        # これ、場合分けが必要だわ
        # 特に取り除くべき要素が、最初か、最初の次か、
        # 最後か、最後から1番目かで、ロジックの実装が変わってしまいそうなので。
        # ====================
        curIndex = 0
        cur = head
        while curIndex < targetIdx-1:
            cur = cur.next
            curIndex += 1
        # edge caseを考える
        if cur.next is None:
            return head
        elif cur.next.next is None:
            cur.next = None
        else:  # 普通のケース
            cur.next = cur.next.next

        return head

# @lc code=end

