class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target=10
        # position=[6,8]
        # speed=[3,2]

        cars = []
        for idx,i in enumerate(position):
            cars.append([position[idx],(target - position[idx])/speed[idx]])
        
        cars.sort(key=lambda c: c[0], reverse=True)
        stack = []

        for i in range(0, len(cars)):
            
            stack.append(cars[i])
            if len(stack) >= 2 and stack[-1][1] <= stack[-2][1]:
                
                print(stack.pop())

        return len(stack)