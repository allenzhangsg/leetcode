from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rightmost_j = -1
        record = (-1, -1)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i] and j > rightmost_j:
                    record = (i, j)
                    rightmost_j = j
                    break
                    # print(record)

        if record != (-1, -1):
            i, j = record
            # print(nums[i], nums[j])
            nums[i], nums[j] = nums[j], nums[i]
            nums[j + 1:] = sorted(nums[j + 1:])
        else:
            nums.sort()


if __name__ == '__main__':
    nums = [1, 2]
    Solution().nextPermutation(nums)
    print(nums)
