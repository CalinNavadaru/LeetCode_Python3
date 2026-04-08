from typing import List


class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = {
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0)
        }
        max_dist = 0
        x, y, direction = 0, 0, 0
        obs = set((o[0], o[1]) for o in obstacles)
        for command in commands:
            if command == -1:
                direction = (direction + 1) % len(directions)
            elif command == -2:
                direction = (direction + len(directions) - 1) % len(directions)
            else:
                for _ in range(command):
                    dx, dy = directions[direction]
                    if (x + dx, y + dy) in obs:
                        break
                    x = x + dx
                    y = y + dy
                max_dist = max(max_dist, x ** 2 + y ** 2)

        return max_dist