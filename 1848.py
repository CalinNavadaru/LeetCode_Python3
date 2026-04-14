from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if len(nums) == 1:
            return 0
        d = len(nums)
        for i in range(0, len(nums)):
            if nums[i] == target and abs(i - start) < d:
                d = abs(i - start)
        return d
