from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l, r = 0, 0
        steps = k

        while steps > 0:
            if len(dq) == 0:
                dq.append(r)
            elif nums[r] < nums[dq[-1]]:
                dq.append(r)
            else:
                while len(dq) > 0 and nums[r] >= nums[dq[-1]]:
                    dq.pop()
                dq.append(r)
            r += 1
            steps -= 1

        output = []
        while l < r <= len(nums):
            max_val_ind = dq[0]
            output.append(nums[max_val_ind])

            if r == len(nums):
                break

            # move l by one step
            if dq[0] == l:
                dq.popleft()
            l += 1

            # move r by one step
            if len(dq) == 0 or nums[r] < nums[dq[-1]]:
                dq.append(r)
            else:
                while len(dq) > 0 and nums[r] >= nums[dq[-1]]:
                    dq.pop()
                dq.append(r)
            r += 1

        return output
