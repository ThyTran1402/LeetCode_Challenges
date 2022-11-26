class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroSize = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeroSize += 1
            elif zeroSize > 0:
                total = nums[i]
                nums[i] = 0
                nums[i-zeroSize] = total
                
#Time/Space complexity: O(N)