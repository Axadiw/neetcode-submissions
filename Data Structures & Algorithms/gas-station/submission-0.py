class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        found_station = -1
        for start_index in range(len(gas)):
            tank = 0
            current_index = start_index
            visited_stations = 0
            while visited_stations < n:
                tank += gas[current_index] - cost[current_index]
                
                if tank < 0:
                    print(f"station {start_index} wont succeed, gas finished at {current_index}")
                    break
                visited_stations += 1
                current_index = (current_index + 1) % n
                
            if visited_stations >= n:
                found_station = start_index
        
        return found_station

        