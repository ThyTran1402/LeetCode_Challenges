class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        for i in range(0, len(nums), 2):
            maxSum += nums[i]
        return maxSum
            
        
#sort the array first
#Time complexity: O(NlogN)
#Space comlexity: O(1)