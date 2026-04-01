from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = [0 for _ in range(len(digits) + 1)]
        val = digits[-1] + 1
        r[len(digits)] = val % 10
        t = val // 10
        for i in range(len(digits) - 2, -1, -1):
            val = digits[i] + t
            r[i + 1] = val % 10
            t = val // 10

        if not t:
            del r[0]
        else:
            r[0] = t
        return r
