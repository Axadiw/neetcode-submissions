class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()

        lowest = 1000
        highest = 0

        for num in nums:
            numSet.add(num)
            lowest = min(num, lowest)
            highest = max(num, highest)
        
        counter = 0
        maxCounter = 0

        isStreak = True
        for i in range(lowest, highest+1):
            if i in numSet:
                if isStreak:
                    counter += 1
                    maxCounter = max(maxCounter, counter)

                isStreak = True
            else:
                isStreak = False
                counter = 1

        return maxCounter
        



        