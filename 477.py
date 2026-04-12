from typing import List


class Solution:

    def totalHammingDistance(self, nums: List[int]) -> int:
        r = 0
        for i in range(32):
            one = zero = 0
            mask = 1 << i
            for num in nums:
                if mask & num:
                    one += 1
                else:
                    zero += 1
            r += one * zero
        return r
