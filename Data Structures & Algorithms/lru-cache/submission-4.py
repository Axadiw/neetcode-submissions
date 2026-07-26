class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.max_len = capacity

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            return self.od[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
        
        self.od[key] = value        

        if len(self.od) > self.max_len:
            self.od.popitem(last=False)
