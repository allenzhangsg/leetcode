class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """iteration"""
        l1, l2 = len(text1), len(text2)
        arr = [[0] * l2] * l1  # wrong way to create 2d array, because * uses shallow copy.
        arr = [[0 for _ in range(l2)] for _ in range(l1)]

        for i in range(l1):
            for j in range(l2):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        arr[i][j] = 1
                    else:
                        arr[i][j] = arr[i - 1][j - 1] + 1
                else:
                    arr[i][j] = max(
                        # arr[i][j],
                        arr[i - 1][j] if i > 0 else 0,
                        arr[i][j - 1] if j > 0 else 0,
                    )
        return arr[l1 - 1][l2 - 1]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """recursion"""
        dp = {}

        def func(i, j) -> int:
            if i < 0 or j < 0:
                return 0

            if f"{i}:{j}" not in dp.keys():
                max_length = 0
                if text1[i] == text2[j]:
                    max_length = max(func(i - 1, j - 1) + 1, max_length)
                else:
                    max_length = max(func(i - 1, j), max_length)
                    max_length = max(func(i, j - 1), max_length)

                dp[f"{i}:{j}"] = max_length
            return dp[f"{i}:{j}"]

        return func(len(text1) - 1, len(text2) - 1)


if __name__ == '__main__':
    print(Solution().longestCommonSubsequence(text1='abcba', text2='abcbcba'))
