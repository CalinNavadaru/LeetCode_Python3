from typing import List, Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = set()
        for key in c:
            if c[key] in s:
                return False
            s.add(c[key])
        return True