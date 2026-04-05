class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r = 0
        while x or y:
            v1 = x & 1
            v2 = y & 1
            if v1 != v2:
                r += 1
            x >>= 1
            y >>= 1

        return r