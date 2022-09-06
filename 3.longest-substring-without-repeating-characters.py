#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        mp = {}
        start = 0
        cur_max = 0
        for i, char in enumerate(s):
            # あ、過去に既出だけど、対照範囲外だから気にしなくていいやつも拾ってしまっているな
            if char in mp and mp[char] >= start:
                start = mp[char] + 1
                mp[char] = i
            else:
                mp[char] = i
                cur_max = max(i-start+1, cur_max)
            print(s[start:i+1])
        return cur_max
    def lengthOfLongestSubstring2(self, s: str) -> int:
        mp = {}
        start = 0
        maxl = 0
        for i, char in enumerate(s):
            if char in mp and start <= mp[char]:  # 既出のものがでてしまった場合
                start = mp[char] + 1
            # 新出 or 今見ている範囲より昔の部分でしか出ていない場合。
            mp[char] = i
            maxl = max(maxl, i - start + 1)
            # print("now: ", s[start:i])
            
        return maxl
# @lc code=end

