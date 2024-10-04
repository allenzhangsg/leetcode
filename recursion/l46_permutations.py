from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        ans = []

        def func(nums, i):
            l = len(nums)
            if i == l:
                output.append(ans.copy())

            for k in range(i, l):
                nums[i], nums[k] = nums[k], nums[i]
                ans.append(nums[i])
                func(nums, i + 1)
                ans.pop()  # back trace
                nums[k], nums[i] = nums[i], nums[k]  # back trace

        func(nums, 0)
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
