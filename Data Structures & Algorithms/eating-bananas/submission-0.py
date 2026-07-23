import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def hours_to_finish(rate):
            hours = 0
            for i in piles:
                hours += math.ceil(i / rate)
            return hours

        while left < right:
            mid = left + (right - left) // 2
            h_s = hours_to_finish(mid)

            if h_s > h:
                # too slow, need a higher rate
                left = mid + 1
            else:
                # fast enough (or exactly enough), try to go slower
                right = mid

        return left