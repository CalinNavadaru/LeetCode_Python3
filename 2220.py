class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        r = 0
        while start or goal:
            v1 = start & 1
            v2 = goal & 1
            if v1 != v2:
                r += 1
            start >>= 1
            goal >>= 1

        return r


d = {1: 2, 3: 3}
print(d.keys())