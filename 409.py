from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        r = 0
        m = 0
        for key in d:
            if d[key] % 2 == 0:
                r += d[key]
            else:
                r += d[key] - 1
                m = 1

        return r + (m > 0)
