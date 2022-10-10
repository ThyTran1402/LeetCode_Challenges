class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        #two pointers approach
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) #find the k steps number
        
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        
#Time complexity: O(N)-> N is the number of elements are reversed
#Space complexity: O(1)
#use reverse() and two pointers approach