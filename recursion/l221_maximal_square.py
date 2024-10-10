from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}

        def func(i, j) -> int:
            nonlocal dp
            if f"{i}:{j}" not in dp:
                if i == 0 or j == 0:
                    return int(matrix[i][j])

                if matrix[i][j] == '0':
                    return 0
                else:
                    a = func(i - 1, j)
                    b = func(i, j - 1)
                    c = func(i - 1, j - 1)

                    dp[f"{i}:{j}"] = min(a, b, c) + 1
            return dp[f"{i}:{j}"]

        max_length = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_length = max(max_length, func(i, j))  # iterate over all possible positions

        return max_length ** 2
