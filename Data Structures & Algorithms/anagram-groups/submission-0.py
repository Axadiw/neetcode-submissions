class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for letter in s:
            if not(letter in hash1.keys()):
                hash1[letter] = 1
            else:
                hash1[letter] += 1

        for letter in t:
            if not(letter in hash2.keys()):
                hash2[letter] = 1
            else:
                hash2[letter] += 1

        return hash1 == hash2

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []

        for single in strs:
            added = False
            for anagram in anagrams:
                if self.isAnagram(single, anagram[0]):                    
                    anagram.append(single)
                    print(f'Dodaję {single} do listy:{anagram}, all anagrams:{anagrams}')
                    added = True
            if not added:
                anagrams.append([single])
                print(f'Dodaję {single} jako nowy anagram, all anagrams:{anagrams}')
        
        return anagrams
        