#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # またできなかった... 
        ans = []
        path = []
        self.dfs(path, 0, candidates,target, ans)
        return ans

    def dfs(self, path, curSum, cands, tgt, ans):
        # もしもすでにtargetを越えていたら終了
        # 次のcandsがなかったら終了
        # 和がtgtになっていたらansに追加        
        if curSum == tgt:
            ans.append(path)
            return 
        
        if curSum > tgt:
            return 
        elif not cands:
            return

        for i, num in enumerate(cands):
            self.dfs(path+[num], curSum+num, cands[i:], tgt, ans)
        
# @lc code=end

