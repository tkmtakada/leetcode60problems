#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
    
    def __init2__(self, k: int, nums: List[int]):
        # k = 1で、nusm が空リストのときがある
        self.k = k
        self.nums = nums
        heapq.heapify(nums)

        while len(self.nums) >= self.k+1:
            heapq.heappop(self.nums)

    def add2(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) >= self.k+1:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

