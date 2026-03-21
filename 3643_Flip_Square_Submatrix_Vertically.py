from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for t in range(0, k // 2):
            for j in range(y, y + k):
                grid[x + t][j], grid[x + k - 1 - t][j] = grid[x + k - 1 - t][j], grid[x + t][j]

        return grid
