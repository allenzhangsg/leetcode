from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = int(l + (r - l) / 2)

            if nums[mid] == target:
                return mid
            elif target > nums[-1]:  # target on the left side
                if nums[mid] > target:  # mid on the left side
                    r = mid - 1
                else:
                    if nums[mid] > nums[-1]:  # mid on the left side
                        l = mid + 1
                    else:  # mid on the right side
                        r = mid - 1

            else:  # target on the right side
                if nums[mid] < target:  # mid on the right side
                    l = mid + 1
                else:
                    if nums[mid] <= nums[-1]:  # mid on the right side
                        r = mid - 1
                    else:  # mid on the left side
                        l = mid + 1
        return -1
