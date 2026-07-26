import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def how_long(k):
            r = 0
            for p in piles:
                r += math.ceil(p/k)
            return r
        
        right = 0
        for p in piles:
            right = max(right,p)
        left = 1
        
        res = right
        while left <= right:
            mid = (right-left)//2 + left
            long = how_long(mid)
            if long > h:
                left = mid + 1
            else:   
                res = mid
                right = mid - 1

        return res