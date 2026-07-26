class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        items_count = len(matrix[0]) * len(matrix)
        def get_item(index):
            cols = len(matrix[0])
            return matrix[index // cols][index % cols]

        left = 0
        right = items_count -1
        
        while left <= right:
            mid_index = (right - left) // 2 + left
            mid = get_item(mid_index)
            # print(f"mid {mid} mid_index: {mid_index} left: {left} right {right}")

            if mid < target:
                # print('target higher')
                left = mid_index + 1
            elif mid > target:
                # print('target lower')
                right = mid_index - 1
            else:
                # print('bingo')
                return True
        return False


        
        