class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for idx, num in enumerate(nums):
            diff[num] = idx

        for idx, num in enumerate(nums):
            if (target - num) in diff and idx != (diff[target - num]):
                return [idx, diff[target - num]]