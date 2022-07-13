#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
        # 各数字の出現頻度はわかった
        # heapでtop kを出していく？？
        # print(mp)
        queue = [] 
        heapq.heapify(queue)
        for elt, freq in mp.items():
            heapq.heappush(queue, (freq, elt))
            if len(queue) >= k+1:
                heapq.heappop(queue)
        return [elt[1] for elt in queue]
# @lc code=end

