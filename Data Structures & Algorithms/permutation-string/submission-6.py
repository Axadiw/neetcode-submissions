class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        if len(s1) > len(s2):
            return False
        
        sorted_s1 = sorted(s1)
        s1_len = len(s1)

        for left in range(0,len(s2) - len(s1)+1):
            sorted_s2_substring = sorted(s2[left:left+s1_len])
            # print(f"checking {sorted_s2_substring} == {sorted_s1}")
            if sorted_s2_substring == sorted_s1:
                return True
        
        return False
        