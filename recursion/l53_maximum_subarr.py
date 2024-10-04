from typing import List


class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:  # recursion: from right to left
        ret = []

        def func(nums, i):
            if i == 0:
                ret.append(nums[i])
                return nums[i]
            else:
                max_sum = nums[i] + max(0, func(nums, i - 1))
                ret.append(max_sum)
                return max_sum

        func(nums, len(nums) - 1)
        print(ret)

        return max(ret)

    def maxSubArray(self, nums: List[int]) -> int:  # record: from left to right
        sum_list = []
        for i in range(len(nums)):
            if i == 0:
                sum_list.append(nums[i])
            else:
                sum_list.append(nums[i] + max(0, sum_list[i - 1]))

        return max(sum_list)
