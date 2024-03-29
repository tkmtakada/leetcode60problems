#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:        
        used = set([])
        def getNextCands(node):
            cands = []
            for word in wordList:
                if word in used:
                    continue
                cnt = 0
                for c, d in zip(node, word):
                    if c != d:
                        cnt += 1
                    if cnt >= 2:
                        break
                if cnt == 1:
                    cands.append(word)
            return cands

        q = [beginWord]
        depth = 0        
        while len(q) > 0:
            depth += 1
            for _ in range(len(q)):
                node = q.pop(0)
                if node == endWord:
                    return depth
                next_nodes = getNextCands(node)                
                used |= set(next_nodes)
                q.extend(next_nodes)
        return 0
    
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # shorteestなのでbfsを使う
        wordList = set(wordList)
        queue = [beginWord]
        usedList = []
        depth = 0
        while len(queue) > 0:
            depth += 1
            len_queue = len(queue)
            for i in range(len_queue):
                # print("queue",queue)
                # print("wordList",wordList)
                # 先頭を取り出して、　子ノードを生成して queueに追加する
                cur = queue.pop(0)
                if cur == endWord:
                    return depth
                # cand, wordList = self.getAdjCand(cur, wordList)
                cand = self.getNextWordList(cur, wordList)
                queue.extend(cand)  # wordListから、自分自身を取り除いたやつを渡す必要あり            
        return 0
    def getAdjCand(self, word, wordList):
        cand = []
        unused = []
        len_word = len(word)
        for w in wordList:
            
            counter = 0
            for i in range(len_word):
                if w[i] != word[i]:
                    counter += 1
                if counter >= 2:
                    break
            if counter == 1:
                cand.append(w)
            else:
                unused.append(w)
        
        return cand, unused
    def getNextWordList(self, w, wordList):
        lst = []
        
        # 方法1
        
        for idx in range(len(w)):
            for s in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = w[:idx] + s + w[idx+1:]
                if nextWord in wordList:                
                    lst.append(nextWord)
                    wordList.remove(nextWord)

        return lst

        # @lc code=end

