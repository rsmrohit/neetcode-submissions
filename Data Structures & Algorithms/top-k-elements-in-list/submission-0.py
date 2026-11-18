import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []  # min-heap of (count, num), holds at most k items

        for num, cnt in counts.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)  # remove the least frequent

        return [num for cnt, num in heap]