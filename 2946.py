from typing import List


class Solution:

    @staticmethod
    def __check_odd(mat: List[List[int]], i: int, j: int, k: int, m: int):
        return mat[i][j] == mat[i][(j + m - k) % m]

    @staticmethod
    def __check_even(mat: List[List[int]], i: int, j: int, k: int, m: int):
        return mat[i][j] == mat[i][(j + k) % m]

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        m = len(mat[0])
        if k % m == 0:
            return True
        k %= m
        for i in range(n):
            if i % 2 == 0:
                checker = Solution.__check_even
            else:
                checker = Solution.__check_odd
            for j in range(m):
                if not checker(mat, i, j, k, m):
                    return False

        return True
