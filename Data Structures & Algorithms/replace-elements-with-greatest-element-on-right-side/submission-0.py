class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        elements = []
        greatest = -1
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) -1:
                elements.append(-1)
            else:
                elements.append(greatest)
            greatest = max(greatest, arr[i])                
        elements.reverse()
        return list(elements)
        