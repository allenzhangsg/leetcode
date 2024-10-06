class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        record = [0] * len(s)
        arr = list(s)

        for i in range(len(arr)):
            c = s[i]
            if len(stack) == 0:
                stack.append(i)
            else:
                if c == "(":
                    stack.append(i)
                else:
                    if s[stack[-1]] == "(":
                        record[i] = 1
                        record[stack.pop()] = 1
                    else:
                        stack.append(i)

        cnt = 0
        max_cnt = 0
        for i in range(len(record)):
            r = record[i]
            if r == 0:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
                continue
            if r == 1:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

        return max_cnt


if __name__ == '__main__':
    print(Solution().longestValidParentheses("()(())"))
    print(Solution().longestValidParentheses("()(()"))
