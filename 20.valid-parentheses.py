#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for p in s:
            if p in ['(', '[', '{']:
                queue.append(p)
            elif p in [')', ']', '}']:
                if len(queue) > 0:
                    r = queue.pop()
                    if self.getCounterpart(p) != r:
                        return False
                else:
                    return False
                

        if len(queue) == 0:
            return True
        else: return False
    
    def getCounterpart(self, s):
        if s == '(':
            return ')'
        elif s == '[':
            return ']'
        elif s == '{':
            return '}'
        if s == ')':
            return '('
        elif s == ']':
            return '['
        elif s == '}':
            return '{'
        
# @lc code=end

