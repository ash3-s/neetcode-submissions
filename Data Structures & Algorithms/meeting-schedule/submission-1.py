"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        if not intervals: return True

        lastEnd = intervals[0].end
        for inter in intervals[1:]:
            if inter.start < lastEnd:
                return False
            
            lastEnd = max(lastEnd, inter.end)
        return True