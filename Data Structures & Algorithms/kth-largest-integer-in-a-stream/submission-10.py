class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-2000]
        self.k = k
        for n in nums:
            self.add(n)
        print('-')

    def add(self, val: int) -> int:
        print(f"adding {val}")
        self.heap.append(val)
        

        i = len(self.heap)-1

        # place correctly
        while self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i // 2]
            self.heap[i // 2] = self.heap[i]
            self.heap[i] = tmp
            i = i // 2
        print(f"a heap: {self.heap}")

        if len(self.heap)-1 > self.k:
            # remove top
            print(f"removing {self.heap[1]}")
            last_val = self.heap.pop()
            self.heap[1] = last_val
            i = 1

            print(f"after adding last element to the top: {self.heap}")
            while (len(self.heap) > i*2 and self.heap[i] > self.heap[i*2]) or (len(self.heap) > i*2+1 and self.heap[i] > self.heap[2*i+1]):
                is_right_child = len(self.heap) > i*2+1
                print(f"i {i} is_right_child {is_right_child}")
                if (not is_right_child or (is_right_child and self.heap[i*2] <= self.heap[i*2+1])) and self.heap[i] > self.heap[i*2]:
                    print(f'exchange with left child {self.heap[2*i]}')
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i]
                    self.heap[2*i] = tmp
                    i = i * 2
                elif len(self.heap) > i*2+1 and self.heap[i] > self.heap[i*2+1]:
                    print(f'exchange with right child {self.heap[2*i+1]}')
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i + 1]
                    self.heap[2*i + 1] = tmp
                    i = i * 2 +1
                else:
                    break


        print(f"heap: {self.heap}")
        return self.heap[1] if len(self.heap) > 1 else 0
        
