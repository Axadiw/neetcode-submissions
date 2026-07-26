class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_val = 0

        if len(s) <= 0:
            len(s)

        for i, s in enumerate(s):
            print(f"s: {s}")
            if s in seen:
                max_val = max(max_val, len(seen.items()))
                print(f"{s} seen already")
                first_index_of_duplicate = seen.get(s)
                items = list(seen.keys())
                print(f"items found: {items}")
                for item in items:
                    if seen[item] < first_index_of_duplicate:
                        print(f"removing {seen[item]}")
                        del seen[item]

            seen[s] = i
        max_val = max(max_val, len(seen.items()))
        print(f"end hashmap{seen}")
        return max_val

        