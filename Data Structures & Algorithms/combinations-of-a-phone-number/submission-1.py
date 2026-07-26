class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }

        ret_array = []
        curr = []
        l = len(digits)
        def helper(i):
            if i > len(digits) - 1:
                if len(curr) == l and l > 0:
                    ret_array.append(''.join(curr.copy()))
                return
            
            for letter in dictionary[digits[i]]:
                curr.append(letter)
                helper(i+1)
                curr.pop()
            
            helper(i+1)

        helper(0)
        return ret_array;

        