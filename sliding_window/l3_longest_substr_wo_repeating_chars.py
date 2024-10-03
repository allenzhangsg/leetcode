# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in [0, 1]:
            return len(s)

        l, r = 0, 1
        length = 1
        max_length = 1

        while l <= r < len(s):
            if s[r] not in s[l:r]:
                length += 1
            else:
                while s[r] in s[l:r]:
                    a = s[l]
                    l += 1
                    if l == r:
                        length = 1
                    elif a != s[r]:
                        length -= 1
            r += 1
            max_length = max(max_length, length)

        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
