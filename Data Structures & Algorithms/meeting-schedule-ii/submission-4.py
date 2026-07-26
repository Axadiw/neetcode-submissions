"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""



class Solution:

    def minMeetingRooms(self, intervals: List[Interval]) -> int:        
        sintervals = sorted(intervals, key=lambda x: x.start)
        
        n = len(intervals)
        i = 0
        rooms = []

        def helper(interval):
            return f"{interval.start}-{interval.end}"

        # print(f"sintervals: {[helper(x) for x in sintervals]}")

        for interval in sintervals:
            if len(rooms) == 0:
                rooms.append(interval)
                # print(f"adding {helper(interval)} as 1st room")
                continue
            
            found_room = False
            for i in range(len(rooms)):
                room = rooms[i]
                # print(f"analyzing if i can fit {helper(interval)} into {helper(room)}")

                if interval.start >= room.end:                    
                    rooms[i] = interval
                    # print(f"{helper(interval)} would fit on id {i}")
                    found_room = True
                    break
            
            if not found_room:
                # print(f"it wont fit, adding as new room")
                rooms.append(interval)

        # print(f"finally rooms: {[helper(x) for x in rooms]}")
        return len(rooms)

        