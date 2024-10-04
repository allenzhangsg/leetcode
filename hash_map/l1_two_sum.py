from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        ret = []
        for i in range(len(nums)):
            if nums[i] in d.keys():
                ret = [i, d[nums[i]]]
            d.update({target - nums[i]: i})

        return ret
