from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def infect(i, j):
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            if i >= 1:
                infect(i - 1, j)
            if i < len(grid) - 1:
                infect(i + 1, j)
            if j >= 1:
                infect(i, j - 1)
            if j < len(grid[i]) - 1:
                infect(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    cnt += 1
                    infect(i, j)

        return cnt
