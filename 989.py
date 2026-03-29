from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        t = 0
        r = []
        for i in range(len(num) - 1, -1, -1):
            v = num[i] + k % 10 + t
            t = v // 10
            r.append(v % 10)
            k //= 10

        while k:
            v = k % 10 + t
            t = v // 10
            r.append(v % 10)
            k //= 10

        if t:
            r.append(t)

        r.reverse()
        return r
