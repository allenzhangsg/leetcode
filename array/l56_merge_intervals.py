from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # sort by the first element

        output = []
        curr = intervals[0]

        for i in range(1, len(intervals)):
            if curr[1] < intervals[i][0]:  # no overlap
                output.append(curr.copy())
                curr = intervals[i]
            else:  # overlap
                curr[1] = max(intervals[i][1], curr[1])  # merge or cover

        output.append(curr.copy())

        return output


if __name__ == '__main__':
    print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
