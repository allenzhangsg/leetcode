from random import randint
from typing import List


class Solution:
    def partition(self, nums: List[int], start, end) -> int:
        pivot = randint(start, end)
        nums[pivot], nums[start] = nums[start], nums[pivot]
        pivot_value = nums[start]

        while start < end:
            while start < end and nums[end] >= pivot_value:  # skip those on the right
                end -= 1

            if start < end:
                nums[start] = nums[end]
                start += 1

            while start < end and nums[start] <= pivot_value:  # skip those on the left
                start += 1

            if start < end:
                nums[end] = nums[start]
                end -= 1

        nums[start] = pivot_value
        return start

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        def quick_sort(nums, start, end):
            if start >= end:
                return

            pivot = self.partition(nums, start, end)
            quick_sort(nums, start, pivot - 1)
            quick_sort(nums, pivot + 1, end)

        quick_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    print(Solution().sortArray([1, 5, 3, 2, 4]))
