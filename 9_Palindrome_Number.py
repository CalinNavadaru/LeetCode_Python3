class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        y = 0
        x_copy = x

        while x_copy:
            x_copy, digit = divmod(x_copy, 10)
            y = y * 10 + digit

        return x == y
