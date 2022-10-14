#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

import heapq
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        heapq.heapify(queue)
        visited = set([])
        i, j = 0, 0
        heapq.heappush(queue, (nums1[i]+nums2[j], i, j))
        ans = []        
        while len(queue) > 0 and len(ans) < k:
            # print(queue)
            _, i, j = heapq.heappop(queue)
            ans.append([nums1[i], nums2[j]])
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(queue, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))

            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(queue, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))
            
        return ans
    def kSmallestPairs2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        heapq.heapify(queue)

        # visited = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]

        # i = j = 0
        def getElt(x,y):
            return (nums1[x] + nums2[y], [x, y])
        elt = getElt(0,0)
        heapq.heappush(queue, elt)
        # visited[0][0] = 1
        visited = set()
        visited.add((0,0))

        ans = []
        for i in range(k):
            front = heapq.heappop(queue)
            x, y = front[1]
            ans.append([nums1[x], nums2[y]])
            if x < len(nums1)-1 and (x+1,y) not in visited:
                elt = getElt(x+1, y)
                heapq.heappush(queue, elt)
                visited.add((x+1, y))
            # print(visited, x, y)
            if y < len(nums2)-1 and (x, y+1) not in visited:
                elt = getElt(x, y+1)
                heapq.heappush(queue, elt)
                # visited[x][y+1] = 1
                visited.add((x, y+1))
            if len(queue) == 0:
                break
        return ans
# @lc code=end

