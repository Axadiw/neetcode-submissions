class Solution:
    def isValid(self, s: str) -> bool:
        letters = []
        for letter in s:
            if letter in ['(', '{', '[']:
                letters.append(letter)

            if letter == ')':
                if len(letters) <= 0:
                    return False
                lastLetter = letters.pop()
                if lastLetter != '(':
                    return False

            if letter == '}':
                if len(letters) <= 0:
                    return False
                lastLetter = letters.pop()
                if lastLetter != '{':
                    return False

            if letter == ']':
                if len(letters) <= 0:
                    return False
                lastLetter = letters.pop()
                if lastLetter != '[':
                    return False
        
        return len(letters) == 0
