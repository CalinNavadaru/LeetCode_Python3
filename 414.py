from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = -(2 ** 32) - 1
        max2 = -(2 ** 32) - 1
        max3 = -(2 ** 32) - 1

        for c in nums:
            if c > max1:
                max3 = max2
                max2 = max1
                max1 = c
            elif max1 > c > max2:
                max3 = max2
                max2 = c
            elif max2 > c > max3:
                max3 = c

        if max3 != -(2 ** 32) - 1:
            return max3
        else:
            return max1
