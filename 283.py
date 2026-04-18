from typing import List


# O(N ** 2)
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(0, len(nums)):
#             if nums[i] == 0:
#                 for j in range(i + 1, len(nums)):
#                     if nums[j] != 0:
#                         nums[i], nums[j] = nums[j], nums[i]
#                         break

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0 and r != l:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
