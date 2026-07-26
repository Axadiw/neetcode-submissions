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

        potential = None
        # print(f"starting search in {self.values[key]} with timestamp {timestamp}")
        while left <= right:
            mid = (right - left)//2 + left
            # print(f"left {left} right {right} mid{mid}"

            if self.values[key][mid][0] > timestamp:
                # print("value too high, search lower")
                right = mid - 1
            elif self.values[key][mid][0] < timestamp:
                # print("value ok, but look higher")
                potential = mid
                left = mid + 1
            else:
                # print(f"bingo {self.values[key][mid][1]}")
                return self.values[key][mid][1]   
        # a = self.values[key][left][1] if self.values[key][left][0] <= timestamp else ""
        a = self.values[key][potential][1] if potential != None else ""
        # print(f"returning {a}")
        return a
