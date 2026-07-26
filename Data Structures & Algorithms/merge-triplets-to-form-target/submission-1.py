class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = False

        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                found = True
                break
        
        if not found:
            return False 

        found = False
        for triplet in triplets:
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                found = True
                break
        
        if not found:
            return False
        
        found = False
        for triplet in triplets:
            if triplet[2] == target[2] and triplet[0] <= target[0] and triplet[1] <= target[1]:
                found = True
                break
        
        return found