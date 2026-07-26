class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(start, length):
            # print(f"starting start {start} length{length} ")
            first_letter = s[start]

            if start+length > len(s):
                return 0

            for letter in s[start+1:start+length]:
                if first_letter != letter:
                    # print(f"start {start} length{length} bad core")
                    return 0

            counter = 1
            left = start - 1
            right = start+length
            while left >= 0 and right<len(s):
                if s[left] == s[right]:
                    # print(f"{s[left]}=={s[right]}")
                    counter += 1
                else:
                    break
                
                left -= 1
                right += 1
            
            return counter
        
        counter = 0
        for i in range(len(s)):
            counter += helper(i,1) + helper(i,2)
        return counter