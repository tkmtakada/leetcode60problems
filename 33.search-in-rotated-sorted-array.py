#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return 
    
    def search2(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if len(nums) == 1 and nums[0] == target: return 0
        if len(nums) == 1 and nums[0] != target: return -1


        # minimumを見つける
        s, e = 0, len(nums)-1        
        # print("finding minimum elt.")
        while s < e:
            m = (s + e) // 2

            # 大小関係
            if nums[s] <= nums[m] and nums[m] < nums[e]:
                # return nums[s]
                break
            elif nums[m] < nums[e] and nums[e] < nums[s]:
                e = m
            elif nums[e] < nums[m] and nums[s] <= nums[m]:
                s = m + 1
        
        idx_min = s
        print("idx_min: ", idx_min)

        # ふつうのbinary search, 存在するかどうか
        # print("starting binary search")
        nums2 = nums[idx_min:] + nums[:idx_min]
        s, e = 0, len(nums2)-1

        if target < nums2[0]: return -1
        elif nums2[-1] < target: return -1
    

        idx_tgt = -1        
        while s < e:
            m = (s + e) // 2
            if nums2[m] == target:
                idx_tgt = m
                break
            elif target < nums2[m]:
                e = m
            elif nums2[m] < target:
                s = m+1
        # 最後だけでloopしょりできないからここで処理
        if nums2[s] == target: idx_tgt = s

        if idx_tgt == -1:
            return -1
        else:
            return (idx_tgt + idx_min) % len(nums2)

# @lc code=end

