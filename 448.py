from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(x for x in range(1, len(nums) + 1))
        for c in nums:
            if c in s:
                s.remove(c)
        return list(s)
