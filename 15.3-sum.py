#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        ans = set([])
        mp = {nums[0]+nums[1]:[[0, 1]]}
        for i in range(2, len(nums)):
            # check if num can be answer
            if (-nums[i]) in mp:
                two_num_lst = mp[-nums[i]]
                for two_num in two_num_lst:
                    k, l = two_num
                    three_nums = [nums[k], nums[l], nums[i]]                    
                    # three_nums.sort()
                    ans.add(tuple(sorted(three_nums)))
            # push into hash map
            for j in range(i):
                two_sum = nums[j] + nums[i]
                if two_sum in mp:
                    mp[two_sum].append([j, i])
                else:
                    mp[two_sum] = [[j, i]]
        return list(ans)
        ans_tuple = list(ans)
        ans_lst = [list(elt) for elt in ans_tuple]
        return ans_lst

# @lc code=end

