class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        found_station = -1
        start_index = 0
        current_index = 0
        visited_stations = 0
        tank = 0          

        if sum(gas) - sum(cost)  < 0:
            return -1

        while visited_stations < n:
            tank += gas[current_index] - cost[current_index]
            if tank < 0:         
                current_index = (current_index + 1) %n            
                start_index = current_index
                visited_stations = 0
                tank = 0
            else:
                visited_stations += 1            
                current_index = (current_index + 1) %n            
            
        
        return start_index

        