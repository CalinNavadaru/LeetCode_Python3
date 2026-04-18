class Solution:
    def mirrorDistance(self, n: int) -> int:
        y = 0
        n_copy = n
        while n_copy:
            n_copy, m = divmod(n_copy, 10)
            y = y * 10 + m

        return abs(n - y)
