from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_dict = dict()

        for index, num in enumerate(nums):
            if (first_index := pair_dict.get(target - num, None)) is not None:
                return [first_index, index]
            pair_dict[num] = index

        return []
