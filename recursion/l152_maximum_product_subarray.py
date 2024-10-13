from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in nums]
        dp[0][0], dp[0][1] = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[i][0] = max(nums[i], dp[i - 1][0] * nums[i])
                dp[i][1] = min(nums[i], dp[i - 1][1] * nums[i])
            else:
                dp[i][0] = max(nums[i], dp[i - 1][1] * nums[i])
                dp[i][1] = min(nums[i], dp[i - 1][0] * nums[i])

        return max(list(map(lambda x: x[0], dp)))
