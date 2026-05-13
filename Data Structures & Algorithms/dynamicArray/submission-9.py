class DynamicArray:    
    def __init__(self, capacity: int):
        self.tmp = []
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.tmp[i]


    def set(self, i: int, n: int) -> None:
        self.tmp[i] = n


    def pushback(self, n: int) -> None:
        if len(self.tmp) == self.capacity: 
            self.resize()
        self.tmp.append(n)

    def popback(self) -> int:
        return self.tmp.pop()
 

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:        
        return len(self.tmp)
        
    
    def getCapacity(self) -> int:   
        print(f'getCapacity teraz ma {self.capacity}')             
        return self.capacity
