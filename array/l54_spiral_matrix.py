from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        ret = []

        up, down, left, right = 0, len(matrix), 0, len(matrix[0])

        while up < down and left < right:
            if up < down:  # always make sure up<down
                for col in range(left, right):
                    ret.append(matrix[up][col])
                up += 1

            if left < right:
                for row in range(up, down):
                    ret.append(matrix[row][right - 1])
                right -= 1

            if up < down:
                for col in range(right - 1, left - 1, -1):
                    ret.append(matrix[down - 1][col])
                down -= 1

            if left < right:
                for row in range(down - 1, up - 1, -1):
                    ret.append(matrix[row][left])
                left += 1

        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
