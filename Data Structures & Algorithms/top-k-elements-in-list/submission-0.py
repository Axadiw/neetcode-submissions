class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        histogram = {}

        for num in nums:
            if num in histogram.keys():
                histogram[num] += 1
            else:
                histogram[num] = 1
        
        items = sorted(histogram.items(), key=lambda x: x[1], reverse=True)

        return list(map(lambda x: x[0], items[0:k]))