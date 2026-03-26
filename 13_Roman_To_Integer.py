class Solution:
    roman_digits = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        if len(s) == 1:
            return Solution.roman_digits[s]
        r = 0
        for i in range(0, len(s)):
            if i < len(s) - 1 and Solution.roman_digits[s[i]] < Solution.roman_digits[s[i + 1]]:
                r -= Solution.roman_digits[s[i]]
            else:
                r += Solution.roman_digits[s[i]]
        return r
