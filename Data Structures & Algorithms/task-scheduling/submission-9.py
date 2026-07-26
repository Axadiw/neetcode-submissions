class Task:
    def __init__(self, task: str, occurences: int):
        self.task = task
        self.occurences = occurences
    
    def __repr__(self):
        return f"task: {self.task} occurences:{self.occurences}"

class Heap:
    def __init__(self, tasks: List[Task]):
        self.heap = [Task(task='Dummy', occurences=-1)]
        for task in tasks:
            
            self.heap.append(task)

        self.heapify()
    
    def add(self, task: Task):
        self.heap.append(task)
        i = len(self.heap)-1

        while i//2>0 and self.heap[i//2].occurences < self.heap[i].occurences:
            self.swap(i,i//2)
            i = i // 2

    def pop(self) -> Task:
        if len(self.heap) == 1:
            return None
        
        if len(self.heap) == 2:
            return self.heap.pop()

        ret_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolite(1)

        return ret_val

    def heapify(self):
        for i in range(len(self.heap), 0, -1):
            self.percolite(i)

    def percolite(self, i):
        while 2*i < len(self.heap):
            if 2*i+1 < len(self.heap) and self.heap[2*i+1].occurences > self.heap[2*i].occurences and self.heap[2*i+1].occurences > self.heap[i].occurences:
                self.swap(2*i+1,i)
                i = 2*i + 1
            elif self.heap[2*i].occurences > self.heap[i].occurences:
                self.swap(2*i,i)
                i = 2*i
            else:
                break


    def swap(self, i,j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 0:
            return 0
        
        counts = {}

        for t in tasks:
            if t not in counts:
                counts[t] = 0
            counts[t] += 1
        
        occurences_tasks = []
        for t in counts.keys():
            occurences_tasks.append(Task(task=t,occurences=counts[t]))
        
        heap = Heap(tasks=occurences_tasks)
        cooldown = deque()
        time = 0

        while len(heap.heap) > 1 or len(cooldown) > 0:
            # print(f"time{time} cooldown: {cooldown} heap: {heap.heap}")
            if len(cooldown) > 0 and time - cooldown[0][1] > n:
                # print(f"time - cooldown[0][1] >= n-1: {time - cooldown[0][1]} > {n+1}")
                heap.add(cooldown.popleft()[0])
            if len(heap.heap) > 1:
                most_popular = heap.pop()
                most_popular.occurences -= 1
                if most_popular.occurences > 0:
                    cooldown.append([most_popular, time])
                print(f'adding task {most_popular.task}')
            else:
                print(f'NOP')
            time += 1

        
        
        return time