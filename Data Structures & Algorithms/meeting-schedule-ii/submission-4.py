"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda u: u.start)
        rooms = []

        i = 0

        for iv in intervals:
            if rooms and rooms[0] <= iv.start:
                heapq.heapreplace(rooms, iv.end)
            else:
                heapq.heappush(rooms, iv.end)

        return len(rooms)

