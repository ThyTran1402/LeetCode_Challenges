class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        array_index = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if i != array_index:
                    nums[i], nums[array_index] = nums[array_index], nums[i]
                array_index += 1
        return nums
    
#in-place swapping approach   
#Time complexity: O(N)
#Space complexity: (1)