#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        heapq.heapify(lst)
        for node in lists:
            if node:  
                heapq.heappush(lst, node.val)
                while node.next:                
                    node = node.next
                    heapq.heappush(lst, node.val)
        ansNode = ListNode()
        curNode = ansNode
        while len(lst) > 0:
            val = heapq.heappop(lst)            
            curNode.next = ListNode(val)
            curNode = curNode.next
        return ansNode.next


        
# @lc code=end

