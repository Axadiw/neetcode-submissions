class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_val = 0
        left = 0

        if len(s) <= 0:
            len(s)

        for i, st in enumerate(s):
            print(f"st: {st}")
            if st in seen:
                max_val = max(max_val, i-left)
                print(f"{st} seen already i {i} left {left}")
                print(f"seen[st] was {seen[st]} setting left to {seen[st]+1}")
                if seen[st] >= left:
                    left = seen[st] + 1

            seen[st] = i
        max_val = max(max_val, len(s)-left)
        print(f"end left: {left} len(s) {len(s)}")
        return max_val

        