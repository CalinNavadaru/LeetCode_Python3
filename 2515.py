from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        min_d = len(words) + 1
        for k in range(0, len(words)):
            if (words[(startIndex + k) % len(words)] == target or
                words[(startIndex - k + len(words)) % len(words)] == target) and k < min_d:
                min_d = k
        if min_d == len(words) + 1:
            return -1
        return min_d
