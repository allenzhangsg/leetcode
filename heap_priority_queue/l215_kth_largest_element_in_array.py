from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return heap[0]


if __name__ == '__main__':
    heap = [2, 1, 4, 2, 1, 4, 2, 5]
    heapq.heapify(heap)
    print(heap)
    print(heapq.heappop(heap))  # min-heap
