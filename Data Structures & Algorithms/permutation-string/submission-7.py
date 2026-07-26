class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        if len(s1) > len(s2):
            return False
        
        s1_histogram = {}
        for s in s1:
            if not (s in s1_histogram):
                s1_histogram[s] = 0
            s1_histogram[s] += 1

        s2_substring_histogram = {}
        for right in range(0,len(s2)):
            left = right - len(s1) + 1
            right_letter = s2[right]

            if not (s2[right] in s2_substring_histogram):
                s2_substring_histogram[right_letter] = 0
            s2_substring_histogram[right_letter] += 1

            if left > 0:
                old_left_letter = s2[left-1]
                s2_substring_histogram[old_left_letter] -= 1
                if s2_substring_histogram[old_left_letter] == 0:
                    del s2_substring_histogram[old_left_letter]

            if s1_histogram == s2_substring_histogram:
                return True
        
        return False
        