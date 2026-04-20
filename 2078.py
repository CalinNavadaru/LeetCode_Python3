from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        d_left = 0
        d_right = 0
        for i in range(len(colors) - 1, -1, -1):
            if colors[i] != colors[0]:
                d_left = i
                break

        for i in range(len(colors)):
            if colors[i] != colors[-1]:
                d_right = len(colors) - i - 1
                break

        return max(d_left, d_right)