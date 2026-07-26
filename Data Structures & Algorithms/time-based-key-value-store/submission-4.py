class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        
        self.values[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        
        left = 0
        right = len(self.values[key]) - 1

        counter = 0
        print(f"starting search in {self.values[key]} with timestamp {timestamp}")
        while left < right and counter <20:
            counter += 1
            mid = (right - left)//2 + left
            print(f"left {left} right {right} mid{mid}")

            if right - left <= 1:
                if self.values[key][right][0] <= timestamp:
                    return self.values[key][right][1]
                if self.values[key][left][0] <= timestamp:
                    return self.values[key][left][1]    
                break

            if self.values[key][mid][0] > timestamp:
                print("value too high, search lower")
                right = mid - 1
            elif self.values[key][mid][0] < timestamp:
                print("value ok, but look higher")
                left = mid
            else:
                print(f"bingo {self.values[key][mid][1]}")
                return self.values[key][mid][1]   
        a = self.values[key][left][1] if self.values[key][left][0] <= timestamp else ""
        print(f"returning {a}")
        return a
