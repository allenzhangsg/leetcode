from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """greedy: the first answer it encounters might not be the optimal"""
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        ans = []
        res = amount + 1

        def helper(index, target):
            nonlocal ans, res
            if index == len(coins):
                if target == 0:
                    res = min(res, len(ans))
                return

            value = coins[index]
            for n in range(target // value, -1, -1):
                ans += [value] * n
                helper(index + 1, target - value * n)
                ans = ans[:len(ans) - n]

        helper(0, amount)
        return -1 if res == amount + 1 else res

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """recursive dp"""
        from functools import lru_cache

        @lru_cache(maxsize=None)  # use this decorator to cache intermediate results
        def dp(target):
            if target == 0:
                return 0
            if target < 0:
                return -1

            min_num = amount + 1
            for c in coins:
                prev = dp(target - c)
                if prev >= 0:
                    min_num = min(min_num, prev + 1)
                else:
                    continue
            if min_num == amount + 1:
                min_num = -1

            return min_num

        return dp(amount)

    def coinChange3(self, coins: List[int], amount: int) -> int:
        """iterative dp"""
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0 and dp[i - c] >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
            if dp[i] == amount + 1:
                dp[i] = -1

        return dp[amount]


if __name__ == '__main__':
    print(Solution().coinChange3([186, 419, 83, 408], 6249))
    # print(Solution().coinChange3([1, 2, 5], 11))
