class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return self.threeSum2([0,0,0,0])

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        sorted_nums = sorted(nums)
        # print(f"sorted: {sorted_nums}")
        
        for i in range(0,len(sorted_nums)-2):
            if i == 0 or i > 0 and sorted_nums[i] != sorted_nums[i-1]:

                j = i+1
                k = len(nums) -1
                while k > j:
                    # print(f"{i}{j}{k}")                    
                    representation = [sorted_nums[i],sorted_nums[j],sorted_nums[k]]
                    my_sum = representation[0] + representation[1] + representation[2]
                    if my_sum == 0:
                        result.append(representation)                        
                        j += 1
                        # k -= 1
                        
                        while k > j and sorted_nums[j] == sorted_nums[j-1]:
                            j += 1
                        while k > j and sorted_nums[k] == sorted_nums[k-1]:
                            k -= 1                            
                    elif my_sum < 0:
                        j += 1
                    else:
                        k -= 1
        return result
        