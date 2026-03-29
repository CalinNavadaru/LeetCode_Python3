from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = strs[0]
        len_r = len(r)
        for i in range(1, len(strs)):
            len_r = min(len_r, len(strs[i]))
            for j in range(len_r):
                if strs[i][j] != r[j]:
                    len_r = j
                    break

        return r[:len_r]
