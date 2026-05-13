class MinStack:

    def __init__(self):
        self.inner = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.inner.append(val)
        
        last_minimum = self.minimum[-1] if len(self.minimum)>0 else 2**31-1
        self.minimum.append(min(last_minimum, val))
        # print(f"push: {self.minimum}")

    def pop(self) -> None:
        # print(f"pop start: {self.minimum}")
        last = self.inner.pop()
        self.minimum.pop()
        # print(f"pop end: {self.minimum}")
        return last

    def top(self) -> int:
        return self.inner[-1]

    def getMin(self) -> int:
        # print(f"get_minimum: {self.minimum}")
        return self.minimum[-1]
        
