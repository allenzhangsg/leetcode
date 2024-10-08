class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        l, r = 0, 0
        target = {}
        pos = []

        for c in t:
            if c not in target:
                target[c] = 0
            target[c] += 1

        def satisfied(target):
            for v in target.values():
                if v > 0:
                    return False
            return True

        while l <= r < length:
            if s[r] in target:
                target[s[r]] -= 1

            while satisfied(target):
                pos.append((l, r))
                if s[l] in target:
                    target[s[l]] += 1
                l += 1

            while l <= r and s[l] not in target:
                l += 1

            r += 1

        min_len = length
        output = ""
        for i, j in pos:
            if j - i < min_len:
                min_len = j - i
                output = s[i:j + 1]

        return output


if __name__ == '__main__':
    print(Solution().minWindow("bba", "ab"))
