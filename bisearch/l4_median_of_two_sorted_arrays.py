from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        left = (m + n + 1) // 2
        right = (m + n) // 2 + 1

        # if m+n is odd, left==right

        def get_kth(nums1, start1, end1, nums2, start2, end2, k):
            len1 = end1 - start1 + 1
            len2 = end2 - start2 + 1

            # always make sure len1<len2
            if len1 > len2:
                return get_kth(nums2, start2, end2, nums1, start1, end1, k)  # switch nums1 and nums2

            if len1 == 0:
                return nums2[start2 + k - 1]

            if k == 1:
                return min(nums1[start1], nums2[start2])

            mid1 = start1 + min(k // 2, len1) - 1
            mid2 = start2 + min(k // 2, len2) - 1

            if nums1[mid1] < nums2[mid2]:
                return get_kth(nums1, mid1 + 1, end1, nums2, start2, end2, k - (mid1 - start1 + 1))
            else:
                return get_kth(nums1, start1, end1, nums2, mid2 + 1, end2, k - (mid2 - start2 + 1))

        return (get_kth(nums1, 0, n - 1, nums2, 0, m - 1, left) + get_kth(nums1, 0, n - 1, nums2, 0, m - 1, right)) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[]))
