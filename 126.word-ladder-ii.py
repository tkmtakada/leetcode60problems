#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import  deque
"""
絶対できてる、
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        # --- UTIL FUNC ---
        abc = list("abcdefghijklmnopqrstuvwxyz")
        def getNextCands(word):
            cands = []
            for idx, s in enumerate(word):
                for c in abc:
                    if c != s:
                        word_ = word[:idx] + c + word[idx+1:]
                        if word_ in wordList and word_ not in used:
                            cands.append(word_)
                        if word_ == endWord:  # 仮に、すでにusednに入っていたとしてもEndwordだけは拾いたいので。
                            cands.append(word_)
            return cands

        # --- DO BFS ---
        q = deque([beginWord])
        used = {endWord:[]}
        isShortestFound = False
        while len(q) > 0 and not isShortestFound:
            for _ in range(len(q)):
                word = q.popleft()
                nextCands = getNextCands(word)
                
                for elt in nextCands:                
                    if elt == endWord:  # --- check if there is endWord in wordList ---
                        isShortestFound = True
                        used[endWord].append(word)
                    else:
                        used[elt] = word
                q.extend(nextCands)
        
        # --- in case there is not path to the endword
        if not isShortestFound:
            return []
        # print(used)
        # --- trace the path and start with startWord
        ans = []
        for elt in used[endWord]:
            reversePath= [endWord]
            while elt != beginWord:
                reversePath.append(elt)
                elt = used[elt]
            reversePath.append(elt)  # add beginWord
            ans.append(reversed(reversePath))
        return ans



# @lc code=end

