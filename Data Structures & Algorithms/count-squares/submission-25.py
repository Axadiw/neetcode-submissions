class CountSquares:

    def __init__(self):
        self.points = set()
        self.pointCounts = {}

    def add(self, point: List[int]) -> None:
        p = (point[0],point[1])
        self.points.add(p)

        if p not in self.pointCounts:
            self.pointCounts[p] = 1
        else:
            self.pointCounts[p] += 1
        

    def count(self, point: List[int]) -> int:
        x,y = point
        ret = 0
        print(f"analyzing point {point}")
        for px,py in self.points:
            print(f"diagonal {(px,py)}, checkif if {(x,py)} and {(py,x)} exist")
            dx = x - px
            dy = y - py

            if (x,py) in self.pointCounts and (px,y) in self.pointCounts and abs(dx) ==abs(dy) and abs(dx) > 0:
                print(f"bingo, returning {self.pointCounts[(px,py)] * self.pointCounts[(x,py)] * self.pointCounts[(px,y)]} self.pointCounts: {self.pointCounts}")
                ret += self.pointCounts[(px,py)] * self.pointCounts[(x,py)] * self.pointCounts[(px,y)]
        return ret

        
