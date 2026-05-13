class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new = t

        if len(s) != len(t):
            return False

        # print(f's to jest {s}')
        for letterA in s:
            # print(f'Will look for letter {letterA} new="{new}"')
            for j in range(0,len(new)):
                # print(f'porównuje {letterA} z {new[j]}')
                if letterA == new[j]:
                    # print('===')
                    # print(f'removing {letterA} at index {j}')
                    # print(new)
                    new = new[:j] + new[j+1:]
                    # print(new)
                    # print('==')
                    break
        
        # print(new)
        return len(new) == 0
        