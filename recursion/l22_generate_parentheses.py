from functools import reduce
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        ans = []

        def process(ans, open_cnt, close_cnt, max_cnt):
            if open_cnt < close_cnt:  # once this happens, stop generating
                return

            if open_cnt == close_cnt == max_cnt:
                output.append(str(reduce(lambda x, y: f"{x}{y}", ans)))

            if open_cnt < max_cnt:
                ans.append("(")
                process(ans, open_cnt + 1, close_cnt, max_cnt)
                ans.pop()  # back trace

            if close_cnt < open_cnt:
                ans.append(")")
                process(ans, open_cnt, close_cnt + 1, max_cnt)
                ans.pop()  # back trace

        process(ans, 0, 0, n)
        return output


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
