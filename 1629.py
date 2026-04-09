from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_time_diff = releaseTimes[0]
        r = 0
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i - 1] > max_time_diff:
                max_time_diff = releaseTimes[i] - releaseTimes[i - 1]
                r = i
            elif releaseTimes[i] - releaseTimes[i - 1] == max_time_diff and keysPressed[r] < keysPressed[i]:
                r = i

        return keysPressed[r]
