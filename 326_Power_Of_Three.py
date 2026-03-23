class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
    # Alternative Solution
    # def isPowerOfThree(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     return 3**19 % n == 0
    