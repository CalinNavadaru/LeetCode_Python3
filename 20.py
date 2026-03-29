class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses = []
        for c in s:
            if c in "{[(":
                open_parentheses.append(c)
            else:
                if not open_parentheses or (c == "}" and open_parentheses[-1] != "{") or \
                        (c == "]" and open_parentheses[-1] != "[") or \
                        (c == ")" and open_parentheses[-1] != "("):
                    return False
                open_parentheses.pop()
        return not open_parentheses
