class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        snums = sorted(nums)
        if snums[0] != 0:
            return 0

        for i in range(1,len(snums)):
            if snums[i] - snums[i-1] != 1:
                return snums[i]-1
        
        return len(snums)