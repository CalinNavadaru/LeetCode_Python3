from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 0 or grid[-1][-1] == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        const = 10 ** 9 + 7
        d = [[(0, 0) for _ in range(m)] for _ in range(n)]
        d[0][0] = (grid[0][0], grid[0][0])
        for j in range(1, m):
            d[0][j] = (d[0][j - 1][0] * grid[0][j], d[0][j - 1][0] * grid[0][j])
        for i in range(1, n):
            d[i][0] = (d[i - 1][0][0] * grid[i][0], d[i - 1][0][0] * grid[i][0])

        for i in range(1, n):
            for j in range(1, m):
                min_right = d[i][j - 1][0] * grid[i][j]
                max_right = d[i][j - 1][1] * grid[i][j]
                min_top = d[i - 1][j][0] * grid[i][j]
                max_top = d[i - 1][j][1] * grid[i][j]
                if min_right > max_right:
                    min_right, max_right = max_right, min_right
                if min_top > max_top:
                    min_top, max_top = max_top, min_top
                d[i][j] = (min(min_top, min_right), max(max_top, max_right))

        return d[-1][-1][1] % const if d[-1][-1][1] >= 0 else -1
