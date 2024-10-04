from typing import List


class Solution:
    def lengthOfLIS2(self, nums: List[int]) -> int:

        def func(nums, i, limit) -> int:
            if i == 0:
                if nums[i] < limit:
                    return 1
                else:
                    return 0

            if nums[i] < limit:
                # with i
                len_with_i = func(nums, i - 1, nums[i]) + 1

                # without i
                len_wo_i = func(nums, i - 1, limit)
                return max(len_with_i, len_wo_i)
            else:  # nums[i] >= limit
                # without i
                return func(nums, i - 1, limit)

        return func(nums, len(nums) - 1, limit=float("inf"))

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.max_len = 0
        dp = {}

        def func(nums, i) -> int:
            if i not in dp:
                i_len = 1
                if i != 0:
                    curr = nums[i]
                    for k in range(0, i):
                        k_len = func(nums, k)
                        prev = nums[k]
                        if curr > prev:
                            i_len = max(i_len, k_len + 1)
                self.max_len = max(self.max_len, i_len)
                dp[i] = i_len
            return dp[i]

        func(nums, len(nums) - 1)
        # print(dp)
        return self.max_len
