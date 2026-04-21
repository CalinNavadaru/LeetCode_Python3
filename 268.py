from typing import List

# 0(N)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         s = sum(nums)
#         return (len(nums) * (len(nums) + 1)) // 2 - s

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums)):
            res += i + 1 - nums[i]
        return res

