class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return_val = []
        for idx_t, t  in enumerate(temperatures):
            print(f'a idx_t: {idx_t} {temperatures[idx_t:]}')
            found = False
            for idx_t1, t1 in enumerate(temperatures[idx_t:]):
                
                if t1 > t:
                    print(f"t {t} t1 {t1},  {idx_t1} {idx_t}")
                    return_val.append(idx_t1 - idx_t + idx_t)
                    found = True
                    break
            if not found:
                return_val.append(0)

        return return_val
        