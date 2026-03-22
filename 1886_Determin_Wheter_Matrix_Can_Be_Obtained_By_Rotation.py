from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        n = len(mat)

        # checking if they are equal (equivalent to a 360 degrees rotation)
        if mat == target:
            return True

        # checking 90 degrees right
        diff = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][n - i - 1]:
                    diff = True
                    break

        if not diff:
            return True

        # checking 180 degrees
        diff = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n - i - 1][n - j - 1]:
                    diff = True
                    break

        if not diff:
            return True

        # checking 90 degrees left
        diff = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n - j - 1][i]:
                    diff = True
                    break

        if not diff:
            return True

        return False
