class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        found = 0
        l = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                found = True
                l += 1
            elif found:
                break
        return l