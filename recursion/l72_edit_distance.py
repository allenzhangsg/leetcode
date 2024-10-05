class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        w1 = list(word1)
        w2 = list(word2)
        dp = {}

        def func(i, j) -> int:
            if f"{i}:{j}" not in dp:
                if i < 0:
                    return j + 1
                if j < 0:
                    return i + 1

                steps1 = func(i - 1, j) + 1  # insert a char to word2
                steps2 = func(i, j - 1) + 1  # insert a char to word1
                steps3 = func(i - 1, j - 1)  # the two chars are identical ,or we need to replace a char
                if w1[i] != w2[j]:
                    steps3 += 1

                dp[f"{i}:{j}"] = min(steps1, steps2, steps3)
            return dp[f"{i}:{j}"]

        return func(len(word1) - 1, len(word2) - 1)


if __name__ == '__main__':
    S = Solution().minDistance('horse', 'ros')
    print(S)
