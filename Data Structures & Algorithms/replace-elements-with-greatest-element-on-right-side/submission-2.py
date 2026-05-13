class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        elements = list(range(len(arr))) 
        greatest = -1
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) -1:
                elements[i] = -1
            else:
                elements[i] = greatest
            greatest = max(greatest, arr[i])                
        # elements.reverse()
        return list(elements)
        