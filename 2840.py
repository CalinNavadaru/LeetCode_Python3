from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[i] for i in range(0, len(s1), 2)) == Counter(s2[i] for i in range(0, len(s1), 2)) and \
            Counter(s1[i] for i in range(1, len(s1), 2)) == Counter(s2[i] for i in range(1, len(s1), 2))
