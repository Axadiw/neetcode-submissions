"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        if n <= 1:
            return True

        sintervals = sorted(intervals, key=lambda x: x.start)

        i = 1
        while i<n:
            if sintervals[i].start < sintervals[i-1].end:
                return False
            i+=1
        
        return True
        



