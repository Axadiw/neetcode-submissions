class MinStack:

    def __init__(self):
        self.inner = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.inner = [*self.inner, val]
        last_minimum = self.minimum[len(self.minimum)-1] if len(self.minimum)>0 else 2**31-1
        self.minimum = [*self.minimum, min(last_minimum, val)]
        # print(f"push: {self.minimum}")

    def pop(self) -> None:
        # print(f"pop start: {self.minimum}")
        *beginning, last = self.inner
        *beginning_m, _ = self.minimum
        self.inner = beginning
        self.minimum = beginning_m
        # print(f"pop end: {self.minimum}")
        return last

    def top(self) -> int:
        return self.inner[len(self.inner) - 1]

    def getMin(self) -> int:
        # print(f"get_minimum: {self.minimum}")
        return self.minimum[len(self.minimum)-1]
        
