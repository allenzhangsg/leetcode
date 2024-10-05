from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # in-place hash
        # Each element within the range of 0 to len should be placed at pos i, where nums[i]==nums[nums[i]-1]

        l = len(nums)

        for i in range(l):
            while 0 <= nums[i] < l and nums[nums[i] - 1] != nums[i]:
                ideal_pos = nums[i] - 1
                nums[ideal_pos], nums[i] = nums[i], nums[ideal_pos]

        for i in range(l):
            if nums[i] != i + 1:
                return i + 1

        return l + 1
