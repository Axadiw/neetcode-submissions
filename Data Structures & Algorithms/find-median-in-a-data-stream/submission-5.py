class MedianFinder:

    def __init__(self):
        self.lower = []
        self.higher = []
        

    def addNum(self, num: int) -> None:
        # print('----addNum----')
        if len(self.lower) == 0 or -self.lower[0] >= num:
            
            heapq.heappush(self.lower, -num)
            # print(f"added to {num} to lower. HIGHER:{self.higher} LOWER:{self.lower}")
        else:
            heapq.heappush(self.higher, num)
            # print(f"added to {num} to higher. HIGHER:{self.higher} LOWER:{self.lower}")

        diff = len(self.higher) - len(self.lower) 
        if diff > 1:
            # higher have more elements
            heapq.heappush(self.lower, -heapq.heappop(self.higher))
            # print(f"moved element from higher to lower. HIGHER:{self.higher} LOWER:{self.lower}")
        if diff < -1:
            # lower have more elements
            heapq.heappush(self.higher, -heapq.heappop(self.lower))
            # print(f"moved element from lower to higher. HIGHER:{self.higher} LOWER:{self.lower}")

    def findMedian(self) -> float:        
        diff = len(self.higher) - len(self.lower)
        # print('--findMedian---')
        # print(f"lower: {self.lower}")
        # print(f"higher: {self.higher}")
        if diff == 0:
            return ((-self.lower[0]) + self.higher[0])/2
        elif diff > 0:
            return self.higher[0]
        else:
            return -self.lower[0]

        
        