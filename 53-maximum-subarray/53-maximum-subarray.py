class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarr = nums[0] #first element in the arr
        currSum = 0
        
        for number in nums:
            if currSum < 0:
                currSum = 0 #reset the currSum
            currSum += number
            maxSubarr = max(maxSubarr, currSum)
        return maxSubarr