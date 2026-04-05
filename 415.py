class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        r = []
        t = 0
        while i >= 0 and j >= 0:
            val = int(num1[i]) + int(num2[j]) + t
            i -= 1
            j -= 1
            t = val // 10
            r.append(str(val % 10))

        while i >= 0:
            val = int(num1[i]) + t
            t = val // 10
            r.append(str(val % 10))
            i -= 1

        while j >= 0:
            val = int(num2[j]) + t
            t = val // 10
            r.append(str(val % 10))
            j -= 1

        if t:
            r.append(str(t))

        return "".join(r[i] for i in range(len(r) - 1, -1, -1))
