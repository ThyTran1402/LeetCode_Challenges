class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr_left, arr_right = 0, sum(nums)
        n = len(nums)
        for i in range(n):
            arr_right -= nums[i]
            if arr_left == arr_right:
                return i
            arr_left += nums[i]
        return -1
    
#Time complexity: O(n)
#Space complexity: O(1)