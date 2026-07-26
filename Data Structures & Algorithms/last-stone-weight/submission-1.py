class Heap:
    def __init__(self, initVals: List[int]):
        self.heap = initVals
        self.heap.append(self.heap[0])
        self.heapify()

    def swap(self, i,j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp
    
    def add(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1 
        print(f"add {self.heap}")
        while i//2>0 and self.heap[i] > self.heap[i//2]:            
            self.swap(i,i//2)
            i = i //2
    
    def pop(self) -> int:
        if len(self.heap) == 1:
            return
        
        if len(self.heap) == 2:
            return self.heap.pop()

        ret_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_up(1)

        return ret_val
    
    def percolate_up(self, i:int):
        while 2*i < len(self.heap):
            has_right_child = 2*i+1 < len(self.heap)
            if has_right_child and self.heap[2*i+1] > self.heap[2*i] and self.heap[2*i+1] > self.heap[i]:
                self.swap(i, 2*i+1)
                i = 2*i+1
            elif self.heap[2*i] > self.heap[i]:
                self.swap(i, 2*i)
                i = 2*i
            else:
                break
    
    def heapify(self):
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            print(f"perlicate {i}")
            self.percolate_up(i)

    def length(self):
        return len(self.heap) - 1
    


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = Heap(initVals=stones)
        while heap.length() > 1:
            print(f"heapheap: {heap.heap}")
            s1 = heap.pop()
            s2 = heap.pop()
            print(f"po s1s2: {heap.heap}")

            if s1>s2:
                heap.add(s1-s2)
            print(f"s1:{s1} s2:{s2} len:{heap.length()} heap {heap.heap}")
        
        print(f"final {heap.heap}")
        return heap.heap[1] if heap.length() == 1 else 0
        