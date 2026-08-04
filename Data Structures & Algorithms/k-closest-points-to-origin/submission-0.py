import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h_dist = []
        heapq.heapify(h_dist)

        def get_euclidean(x, y):
            return math.sqrt(x ** 2 + y ** 2)
        
        for point in points:
            if len(h_dist) < k:
                heapq.heappush(h_dist, (-get_euclidean(point[0], point[1]), point))
            else:
                heapq.heappushpop(h_dist, (-get_euclidean(point[0], point[1]), point))
        
        return [point[1] for point in h_dist]