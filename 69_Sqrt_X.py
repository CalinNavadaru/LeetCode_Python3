class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        st = 1
        dr = x - 1
        while st <= dr:
            m = (st + dr) // 2
            if m * m == x:
                return m
            elif m * m > x:
                dr = m - 1

            else:
                st = m + 1

        return st - 1
