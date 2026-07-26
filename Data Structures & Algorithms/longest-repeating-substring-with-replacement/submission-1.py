class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_map = {}
        max_len = 0
        left = 0

        def remove_oldest():
            # print(f"will remove item at index {left} from {window_map.items()}")
            for item in window_map.items():
                found = False
                for idx,i in enumerate(item[1]):
                    # print(f"looking for item {left} in {item[1]} i={i}")
                    if i == left:
                        # print(f"removing {item[1][idx]} from {item}")
                        item[1].pop(idx)
                        found = True
                        break
                
                if found:
                    break

        def cost_acceptable():
            cost = 0
            
            a = sorted(window_map.items(), key=lambda c: len(c[1]))[:-1]
            # print(f"calculating acceptable cost for sorted {a}")
            for item in a:
                cost += len(item[1])
                if cost > k:
                    return False
            
            return True

        for right in range(len(s)):
            if not (s[right] in window_map):
                window_map[s[right]] = []

            window_map[s[right]].append(right)
            # print(f"added {s[right]}, current window_map: {window_map}")

            if cost_acceptable():                
                max_len = max(max_len, right - left + 1)
                # print(f"cost acceptable, maxlen = {max_len}")
            else:
                # print(f'cost not acceptable for {window_map}')
                while not cost_acceptable():                    
                    remove_oldest()
                    left += 1
                # print(f"window after cleaning: {window_map}")
    
        return max_len
