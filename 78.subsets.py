#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # bit search
        N = 2 ** len(nums)
        for i in range(N):
            lst = []
            for k in range(len(nums)):
                if (i & (1<<k))==1<<k:
                    lst.append(k)
            # print(lst)
            ans.append([nums[idx] for idx in lst])    
            
        return ans
    
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        N = len(nums)
        for k in range(1, N+1):
            path = []
            self.dfs(path, nums, k, ans)
        return ans
    
    def dfs(self, path, nums, k, ans):
        # もう長さがKになった or K未満だけど、numsがない
        if len(path) == k:
            ans.append(path)
            return 
        elif not nums:
            return 
        
        # ここにいるってことは、まだ長さK未満で
        # 使える数字もnumsに残っている
        for i, num in enumerate(nums):
            self.dfs(path+[num], nums[i+1:], k, ans)
# @lc code=end

