class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for letter in s:
            # print(f'szukam {letter} hash1: {hash1}')
            if not(letter in hash1.keys()):
                hash1[letter] = 1
            else:
                hash1[letter] += 1
                # print(f'zinkrementowalem {hash1}')

        for letter in t:
            if not(letter in hash2.keys()):
                hash2[letter] = 1
            else:
                hash2[letter] += 1

        # print('---')
        # print(hash1)
        # print(hash2)
        return hash1 == hash2


    def isAnagram2(self, s: str, t: str) -> bool:
        new = t

        if len(s) != len(t):
            return False

        for letterA in s:
            for j in range(0,len(new)):
                if letterA == new[j]:
                    new = new[:j] + new[j+1:]
                    break
        return len(new) == 0
        