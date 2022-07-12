#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 方針: prevも保存しておく
        if not head: return None
        if not head.next: return head

        # 考えるべきケース
        # 1,1   同じ数字だけで終わる

        dummy = ListNode('#', head)
        prev, cur = dummy, head

        while cur and cur.next:
            if cur.next.val == cur.val:
                # 3, 3, 3, 1  ちゃんと違う数字出てくる
                # 3, 3, 3　　同じ数字だけで終わる
                # 3, 3  のこりふたつ
                start = cur
                val = start.val
                while cur.next and cur.next.val == val:
                    cur = cur.next
                
                # ここがポイント、ポインターを意識して、headからのつながりを見失わない。
                prev.next = cur.next  # cur.nextはNoneか、次の値、prevはまだ動かさない
                cur = prev.next
            else:
                cur, prev = cur.next, cur
        return dummy.next

# @lc code=end

