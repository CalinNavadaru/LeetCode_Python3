from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        for val in nums:
            if val % 3:
                c += 1
        return c