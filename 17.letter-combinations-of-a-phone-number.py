#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        len_digits = len(digits)
        words = {"2":["a", "b", "c"],
                 "3":["d", "e", "f"],
                 "4":["g", "h", "i"],
                 "5":["j","k", "l"],
                 "6":["m","n", "o"],
                 "7":["p", "q", "r", "s"],
                 "8":["t", "u", "v"],
                 "9":["w", "x", "y", "z"]}
        ans_lst = []
        # do recursivbe
        def dfs(depth, path):
            # termination condition
            if depth >= len_digits:
                ans_lst.append(path) # TODO
                return 
            
            for s in words[digits[depth]]:
                dfs(depth+1, path+s)
        
        dfs(0, "")
        if ans_lst[0] == "":
            return []
        else:
            return ans_lst




# @lc code=end

