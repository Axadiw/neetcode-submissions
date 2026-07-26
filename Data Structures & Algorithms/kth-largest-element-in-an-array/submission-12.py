class Heap:
    def __init__(self, init_vals: List[int]): # max_heap
        self.heap = [0]+init_vals
        self.heapify()

    def heapify(self):
        for i in range(len(self.heap)//2,0,-1):
            self.percolite(i)

    def pop(self):
        ret_val = self.heap[1]
        last_val = self.heap.pop()
        if len(self.heap) > 1:
            self.heap[1] = last_val
            self.percolite(1)

        return ret_val
    
    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def percolite(self, i: int):
        while 2*i < len(self.heap):
            if 2*i+1 < len(self.heap) and self.heap[2*i+1] > self.heap[2*i] and self.heap[2*i+1] > self.heap[i]:
                self.swap(i, 2*i+1)
                i = 2*i+1
            elif self.heap[2*i] > self.heap[i]:
                self.swap(i, 2*i)
                i = 2*i
            else:
                break

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap(init_vals=nums)
        for i in range(k-1):
            heap.pop()
        return heap.pop()
        