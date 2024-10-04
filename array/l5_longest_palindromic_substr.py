from functools import reduce


class Solution:
    def longestPalindrome(self, s: str) -> str:
        arr = "#" + "#".join(list(s)) + "#"

        def manacher(arr) -> str:
            l = len(arr)
            maxC = 0
            maxR = 0

            record = [0] * l

            for i in range(1, l):
                if i > maxC + maxR:  # normal approach
                    r = 1
                    while i - r >= 0 and i + r < l and arr[i - r] == arr[i + r]:
                        record[i] = r
                        r += 1
                else:
                    j = maxC - (i - maxC)
                    jL = j - record[j]

                    if jL > maxC - maxR:
                        record[i] = record[j]
                    elif jL < maxC - maxR:
                        record[i] = j - (maxC - maxR)
                    else:
                        r = j - (maxC - maxR)
                        while i - r >= 0 and i + r < l and arr[i - r] == arr[i + r]:
                            record[i] = r
                            r += 1
                if record[i] > maxR:
                    maxR = record[i]
                    maxC = i
            output = arr[maxC - maxR: maxC + maxR + 1]
            return reduce(lambda x, y: f"{x}{y}", filter(lambda x: x != "#", output))

        return manacher(arr)


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("bb"))
