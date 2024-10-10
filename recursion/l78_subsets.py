from collections import deque
from typing import List


class Solution:
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """DFS: using recursion + loop"""
        res = []
        path = []

        def dfs(index):
            nonlocal res, path, nums
            res.append(path.copy())

            if index == len(nums):
                return

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()  # back trace

        dfs(0)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """BFS: using queue + loop"""
        queue = deque()
        output = set()
        subset = []
        queue.append(subset)

        while True:
            curr_set = queue.popleft()
            if len(curr_set) == len(nums):
                break

            output.add(tuple(sorted(curr_set)))

            for n in nums:
                if n not in curr_set:
                    curr_set_cp = curr_set.copy()
                    curr_set_cp.append(n)
                    queue.append(curr_set_cp)

        output = [list(sub_set) for sub_set in output]
        output.append(nums.copy())

        return output


if __name__ == '__main__':
    print(Solution().subsets2([1, 2, 3]))
