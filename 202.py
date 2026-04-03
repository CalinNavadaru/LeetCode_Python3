class Solution:

    @staticmethod
    def compute_sum_square_digits(n: int):
        y = 0
        while n:
            y += (n % 10) ** 2
            n //= 10
        return y

    def isHappy(self, n: int) -> bool:
        found_numbers = set()
        while n not in found_numbers:
            val = Solution.compute_sum_square_digits(n)
            if val == 1:
                return True
            found_numbers.add(n)
            n = val

        return False
