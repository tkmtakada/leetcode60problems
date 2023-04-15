#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def getCircumference(matrix):
            m = len(matrix)
            n = len(matrix[0])
            circumference = matrix[0] + \
                [matrix[i][n-1] for i in range(1,m)] + \
                [matrix[m-1][j] for j in range(n-1, 0)] + \
                [matrix[k][0] for k in range(m-1, 0)]

            small_m = []
            for l in range(1, m-1):
                small_m += matrix[l][1:n-1]
            return circumference, small_m

        ans = []
        while True:
            circumference, small_m = getCircumference(matrix)
            ans += circumference
            matrix = small_m
            print(small_m)
            # if (len(small_m) == 1) or (len(small_m[0]) == 1):
            #     break
            if (len(small_m) == 1) and (len(small_m[0]) == 1):
                ans += small_m  # small_m = [5]
                break
            elif (len(small_m) == 1):
                ans += small_m[0]  # small_m = [[1,2,3]]
                break
            elif (len(small_m[0]) == 1):                
                ans += [lst[0] for lst in small_m]
                break
        # 最後に残った特殊ケースを処理する
        return ans
# @lc code=end

