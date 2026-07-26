class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 = [1,2,5,6,7,8,8,8,8,9,11,25,30,24]
        # nums2 = [2,6,13,16,20]

        length_1 = len(nums1)
        length_2 = len(nums2)
        length_12 = length_1 + length_2
        if len(nums1) > len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp

        
        
        #nums1 is smaller

        left = 0 
        right = len(nums1)

        print(f"nums1 = {nums1}")
        print(f"nums2 = {nums2}")
        
        counter = 0
        while left <= right and counter < 20000000000000:
            counter += 1
            mid_nums1 = left + (right - left) // 2 
            mid_nums2 = length_12 // 2 - mid_nums1
            print('- --------')
            print(f"mid_nums1 {mid_nums1} nums1: {nums1[:mid_nums1]}  {nums1[mid_nums1:]}")
            print(f"mid_nums2 {mid_nums2} nums2: {nums2[:mid_nums2]}  {nums2[mid_nums2:]}")

            left1 = nums1[mid_nums1-1] if len(nums1[:mid_nums1]) >0 else -float('inf')
            right1 = nums1[mid_nums1] if len(nums1[mid_nums1:]) >0 else float('inf')
            left2 = nums2[mid_nums2-1] if len(nums2[:mid_nums2]) >0 else -float('inf')
            right2 = nums2[mid_nums2] if len(nums2[mid_nums2:]) >0 else float('inf')
            print(f"left1 {left1} right1 {right1} left2 {left2} right2 {right2}")

            if left1 <= right2 and right1 >= left2:
                print("good division")
                left = max(left1,left2)
                right = min(right1,right2)
                break
            elif left1 > right2:                
                right = mid_nums1 - 1
                print(f'left1 > right2, setting right to {right} (left will be {left})')
            else:                
                left = mid_nums1 + 1
                print(f'else, setting left to {left} (right will be {right})')
        
        return (left + right)/2 if length_12 % 2 == 0 else right