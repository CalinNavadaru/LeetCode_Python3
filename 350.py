from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []
        d = Counter(nums1)
        for val in nums2:
            if d.get(val, 0) > 0:
                r.append(val)
                d[val] -= 1
        return r
