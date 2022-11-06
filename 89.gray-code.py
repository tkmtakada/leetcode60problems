#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0,1]
        prev = self.grayCode(n-1)
        diff = 2**(n-1)
        return prev + [elt+diff for elt in reversed(prev)]
    def grayCode2(self, n: int) -> List[int]:
        # 参考になる　https://leetcode.com/problems/gray-code/solutions/1308570/python-short-recursive-solution-explained/
        def my_binalize(num, digits):
            binnum = bin(num)[2:]
            if len(binnum) < digits:
                binnum = '0'*(digits-len(binnum)) + binnum
            return binnum
        num_lst = [my_binalize(num, n) for num in range(1, 2**n-1)]
        
        ans = []
        visited = set([])
        def flip(argnum, i):
            if argnum[i] == '1':
                # argnum[i] = '0'
                argnum = argnum[:i] + '0' + argnum[i+1:]
            elif argnum[i] == '0':
                # argnum[i] = '1'
                argnum = argnum[:i] + '1' + argnum[i+1:]
            return argnum
        def dfs(path):
            cur = path[-1]
            # visitedを記録
            visited.add(cur)
            
            # 終了条件
            if len(visited) == 2**n:
                if cur in [2**j for j in range(n-1)]:
                    return path
                else:
                    return

            # dfs
            cands = filter(lambda x: x not in visited, [flip(cur, i) for i in range(n)])
            for next_num in cands:                
                ans = dfs(path+[next_num])
                if ans:
                    return ans
                visited.remove(next_num)
                            
        dfs('0'*n)
        return ans

        
# @lc code=end

