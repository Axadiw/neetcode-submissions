class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0,0

        meeting_point = -1
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                meeting_point = slow
                break

        slow2 = 0

        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow2