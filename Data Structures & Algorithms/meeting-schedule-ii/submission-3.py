"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval.start)

        # End times of meetings currently occupying rooms
        min_heap = []

        for interval in intervals:
            # The earliest-ending room is available
            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)

            # Assign the current meeting to a room
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)