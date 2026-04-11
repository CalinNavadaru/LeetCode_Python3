from typing import List


#
# 0(N * log(M)) N - # of lines; M - # of columns
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         r = 0
#         for i in range(len(grid)):
#             left = 0
#             right = len(grid[i]) - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if grid[i][mid] < 0:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#
#             r += len(grid[i]) - left
#
#         return r
#


# 0(N + M) N - # of lines; M - # of columns
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r = 0
        i = len(grid) - 1
        j = 0
        while i >= 0 and j <= len(grid[i]) - 1:
            if grid[i][j] < 0:
                r = len(grid[i]) - j
                i -= 1
            else:
                j += 1
        return r
