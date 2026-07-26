class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return_val = [0]* len(temperatures)
        days_waiting_for_warmer_temp = []

        if len(temperatures) <= 1:
            return [0]*len(temperatures)

        for idx_t, t  in enumerate(temperatures):
            print(f'analyzing {[idx_t, t]}, current days_waiting_for_warmer_temp = {days_waiting_for_warmer_temp}')
            if len(days_waiting_for_warmer_temp) == 0:
                print(f'append {[idx_t, t]}')
                days_waiting_for_warmer_temp.append([idx_t, t])
                continue

            while len(days_waiting_for_warmer_temp) > 0 and t > days_waiting_for_warmer_temp[-1][1]:
                day = days_waiting_for_warmer_temp.pop()
                r = idx_t - day[0]
                print(f'adding to return value {r} idx: {day[1]}')
                return_val[day[0]] = r 

            print(f'append {[idx_t, t]}')
            days_waiting_for_warmer_temp.append([idx_t, t])

        print(f"left: {days_waiting_for_warmer_temp}")
        return return_val    


    def dailyTemperatures_n2(self, temperatures: List[int]) -> List[int]:
        return_val = []
        for idx_t, t  in enumerate(temperatures):
            found = False
            for idx_t1, t1 in enumerate(temperatures[idx_t:]):
                
                if t1 > t:
                    return_val.append(idx_t1)
                    found = True
                    break
            if not found:
                return_val.append(0)

        return return_val
        