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
        
        ret = ""
        for item in self.values[key]:
            if item[0] <= timestamp:
                ret = item[1]
            else:
                break
        
        return ret
        
