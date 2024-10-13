class Solution:
    def decodeString(self, s: str) -> str:
        chars = list(s)
        pairs = {}
        stack = []
        for i in range(len(chars)):
            c = chars[i]
            if c == "[":
                stack.append(i)
            elif c == "]":
                left_ind = stack.pop()
                pairs[left_ind] = i

        def helper(i, j) -> list:  # concatenating strings is very expensive. use list then join elements
            if i == j:
                return []

            k = i
            str_part = []
            num = 0
            ans: list = []

            while i <= k < j:
                if chars[k].isalpha():
                    str_part.append(chars[k])
                    k += 1
                elif chars[k].isdigit():
                    num = 10 * num + int(chars[k])
                    k += 1
                elif chars[k] == "[":
                    right_ind = pairs[k]
                    ans.append("".join(str_part))
                    ans += num * helper(k + 1, right_ind)
                    k = right_ind + 1
                    num = 0
                    str_part = []
                else:
                    continue

            if len(str_part) > 0:
                ans.append("".join(str_part))  # join: efficient way to convert list to string
            return ans

        return "".join(helper(0, len(s)))


if __name__ == '__main__':
    print(Solution().decodeString("2[abc]3[cd]ef"))
