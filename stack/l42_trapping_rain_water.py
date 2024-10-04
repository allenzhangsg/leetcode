from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # monotonically decreasing
        output = 0

        for i in range(len(height)):
            if len(stack) == 0:
                stack.append(i)
            elif height[i] < height[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and height[i] > height[stack[-1]]:
                    p = stack.pop()
                    right = i
                    if len(stack) > 0:
                        left = stack[-1]
                        v = (min(height[right], height[left]) - height[p]) * (right - left - 1)
                        output += v
                stack.append(i)

        return output


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
