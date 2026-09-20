
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.q = list(nums)
        # print(self.q, nums)
        while len(self.q) > k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        if len(self.q) < self.k:
            heapq.heappush(self.q, val)
        else:
            heapq.heappushpop(self.q, val)
        return min(self.q)

