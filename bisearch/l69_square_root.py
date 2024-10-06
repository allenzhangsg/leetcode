class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x
        l, r = 1, x

        while l < r:
            mid = int(l + (r - l) / 2)
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid > x:
                r = mid
            else:
                l = mid + 1

        return -1


if __name__ == '__main__':
    # "Can you use debug in an IDE?"
    print(Solution().mySqrt(6))
