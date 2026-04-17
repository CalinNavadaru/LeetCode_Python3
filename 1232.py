from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        if not coordinates[0][0] - coordinates[1][0]:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
        else:
            a = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
            b = (coordinates[1][1] * coordinates[0][0] - coordinates[0][1] * coordinates[1][0]) / (
                (coordinates[0][0] - coordinates[1][0]))

            for i in range(2, len(coordinates)):
                if a * coordinates[i][0] + b != coordinates[i][1]:
                    return False
        return True
