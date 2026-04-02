from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = set()

        for val in nums:
            if val not in d:
                d.add(val)
            else:
                return val

        return -1