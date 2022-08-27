#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        2022/08/27

        方針：各単語が入りる場所にて、直前の一個がTrueだったら
        その言葉が入る場所の最後尾もTrueにする
        """        
        dp = [False ] * len(s + 1)  # 先頭に一個必要
        dp[0] = True

        for i in range(1, len(s)+1):
            # candの中にちょうどいいやつがいればTrue
            for word in wordDict:
                len_word = len(word)

                if (i - len_word) > 0 and dp[i - len_word] == True:
                    dp[i] = True
                
        
        return dp[-1]
    
    def wordBreak2 (self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)] 
        dp[0] = True

        for idx in range(1, len(dp)):
            for w in wordDict:
                len_w = len(w)

                if s[idx-len_w:idx] == w and dp[idx-len_w] == True:
                    dp[idx] = True
        return dp[-1]

    # ======================
    #        DPでいけるらしい 
    # ======================
    def wordBreak_answer(self, s: str, wordDict: List[str]) -> bool:
        # DPで解く
        
        lst = [False] * (len(s) + 1)
        lst[0] = True
        
        for idx in range(len(s)):
            for w in wordDict:
                # もし今のindexまでの位置に w を当てはめることができて
                # なおかつ、wが入る位置の一つまえの場所がTrueなら、
                # 今のidxにTrueを入れる
                len_w = len(w)                
                if s[idx-len_w+1:idx+1] == w and lst[idx+1-len_w]:
                    # print(s[idx-len_w+1:idx+1])
                    # print(lst)
                    lst[idx+1] = True
        # print(lst)
        return lst[-1]

# @lc code=end

