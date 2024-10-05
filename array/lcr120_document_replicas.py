from typing import List


class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        l = len(documents)
        nums = documents

        for i in range(l):
            while nums[i] != nums[nums[i]]:
                ideal_pos = nums[i]
                nums[i], nums[ideal_pos] = nums[ideal_pos], nums[i]

            if nums[i] == nums[nums[i]] and nums[i] != i:
                return nums[i]


if __name__ == '__main__':
    print(Solution().findRepeatDocument([2, 5, 3, 0, 5, 0]))
