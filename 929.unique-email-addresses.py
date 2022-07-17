#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueAddress = {}
        for email in emails:
            localName, domain = email.split("@")
            # +までをみる
            for i in range(len(localName)):
                if localName[i] == "+":
                    localName = localName[:i]
                    break
            # dotをremove
            localName = localName.replace(".", "")

            actualAddress = localName + "@" + domain
            if actualAddress in uniqueAddress:
                pass
            else:
                uniqueAddress[actualAddress] = 1
        ans = len(uniqueAddress.keys())
        return ans
# @lc code=end

