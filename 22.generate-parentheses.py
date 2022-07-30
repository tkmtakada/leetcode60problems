#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        L = '('
        R = ')'
        ans = []
        path = []
        n_left = n_right = n  # 残っている数
        self.dfs(path, n_left, n_right, ans)
        return ans
    def dfs(self, path, n_left, n_right, ans):
        # 終了条件
        # n_rightが0
        if n_right == 0:
            ans.append("".join(path))
        
        if n_left > 0:
            self.dfs(path + ['('], n_left-1, n_right, ans)
        
        if n_right > 0 and n_left < n_right:
            self.dfs(path+[')'], n_left, n_right-1, ans)
        
# @lc code=end

