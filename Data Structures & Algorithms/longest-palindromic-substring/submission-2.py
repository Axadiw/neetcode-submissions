class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        def helper(start, length):
            nonlocal longest
            
            # print(f"will start {start} with length {length}")
            if start+length > len(s):
                # print(f"ending start {start} with length {length} - too long")
                return
            i=start

            first_letter = s[start]
            for letter in s[start+1:start+length]:
                if letter != first_letter:
                    # print(f"ending start {start} with length {length} - bad core")
                    return
            
            if len(s[start:start+length]) > len(longest):
                longest = s[start:start+length]

            left = start - 1
            right = start+length
            while left >= 0 and right < len(s):
                # print(f'for core {s[start:start+length]} checking indexes {left}:{right} ({s[left]} and {s[right]})')
                if s[left] == s[right]:
                    if len(s[left:right+1]) > len(longest):
                        # print(f"using {s[left:right+1]} as new longst")
                        longest = s[left:right+1]
                else:
                    break
                

                left -= 1
                right += 1
            # print(f"finish start {start} with length {length}")

            
        for i in range(len(s)):
            helper(i,1)
            helper(i,2)
        
        return longest
            
        