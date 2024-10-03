from functools import reduce
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    print(nums)
    ret = set()

    for k in range(len(nums)):
        target = -nums[k]
        if k == 0 or nums[k] != nums[k - 1]:  # skip target duplicates
            l, r = k + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    result = reduce(lambda x, y: f"{x},{y}", sorted([nums[k], nums[l], nums[r]]))
                    ret.add(result)
                    l += 1
                    r -= 1

    return [list(map(lambda x: int(x), pair.split(","))) for pair in ret]


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
