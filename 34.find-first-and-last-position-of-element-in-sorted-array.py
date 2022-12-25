#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s, e = 0, len(nums)-1
        isFound = False        
        # 存在するかどうか判定
        while s < e:
            m = (s + e) // 2
            if nums[m] == target:
                ifFound = True
                break
            
            if nums[m] < target:
                s = m+1
            else:  # nums[m] > target
                e = m-1
        
        if not isFound:
            return [-1, -1]

        # when target was found
        # Edgeを探す
        s1, e1 = 0, m
        s2, e2 = m, len(nums)-1

        while s1 < e1:
            m1 = (s1+e1) // 2
            if nums[m1] == target:
                e1 = m1
            elif nums[m1] < target:
                s1 = m1+1
            else: # それ以外はありえない、ここにはこない
                pass  
        # while文を抜けた時、そこは左端のはず
        begin = s1

        while s2 < e2:
            m2 = (s2+e2) // 2
            if nums[m2] == target:
                s2 = m2
            elif nums[m2] > target:
                e2 = m2-1
            else: # それ以外はありえない、ここにはこない
                pass  
        # while文を抜けた時、そこは左端のはず
        end = e2

        return [s1, e2]
# @lc code=end

