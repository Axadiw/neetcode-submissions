class PointItem:
    def __init__(self, point: List[int]):
        self.point = point
        self.distance = (math.pow(point[0],2) + math.pow(point[1],2))

class Heap: # max heap    
    def __init__(self, points: List[List[int]]):
        self.heap = [PointItem([0,0])]
        for item in points:
            self.heap.append(PointItem(item))
        self.heapify()
    
    def swap(self, i,j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp
    
    def pop(self):
        ret_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_down(1)

        return ret_val
    
    def heapify(self):
        for i in range(len(self.heap)//2,0,-1):
            self.percolate_down(i)

    def percolate_down(self, i):
        while i*2 < len(self.heap):
            if i*2+1 < len(self.heap) and self.heap[2*i+1].distance > self.heap[2*i].distance and self.heap[2*i+1].distance > self.heap[i].distance:
                #right
                # print('swapuje right')
                self.swap(i,2*i+1)
                i = 2*i+1
            elif self.heap[2*i].distance > self.heap[i].distance:   
                # print('swapuje left')
                self.swap(i,2*i)
                i = 2*i
            else:
                break

    


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = Heap(points)
        # print(f"init heap: {[x.point for x in heap.heap]}")

        while len(heap.heap)-1 > k:
            # print(f"popuje {heap.heap[1].point}")
            heap.pop()
        
        return [x.point for x in heap.heap][1:]