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
        
        # res = right
        counter = 0
        while left < right:
            counter += 1
            mid = (right-left)//2 + left
            long = how_long(mid)
            print(f"left {left} right {right} mid {mid} how_long(mid) {long}")
            if long > h:
                left = mid + 1
                print(f"long ({long}) > h ({h}), moving left to mid ({mid})")
            elif long < h:            
                right = mid
                print(f"long ({long}) < h ({h}), moving right to mid ({mid})")
            else:   
                print("Bingo")
                right = mid

        return left