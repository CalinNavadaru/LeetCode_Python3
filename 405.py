class Solution:
    def toHex(self, num: int) -> str:
        hex_map = "0123456789abcdef"
        if num == 0:
            return "0"
        if num < 0:
            num = num & 0xFFFFFFFF
        result = []
        while num:
            result.append(hex_map[num & 0xF])
            num = num >> 4
        return "".join(result[::-1])
