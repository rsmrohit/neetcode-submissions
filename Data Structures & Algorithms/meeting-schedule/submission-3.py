"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda u: u.start)

        # assume sorted intervals
        i = 0
        curr_val = -1

        while i < len(intervals):

            if intervals[i].start < curr_val:
               return False

            curr_val = intervals[i].end

            i+=1

        return True 

