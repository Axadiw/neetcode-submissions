class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for letter in s:
            if letter == '(':
                low += 1
                high += 1
            elif letter == ')':
                low -= 1
                high -= 1
            else:
                low -= 1 # assume it was )
                high += 1 # assume it was (
            
            if high < 0:
                return False
            if low < 0:
                low = 0

        
        return low == 0