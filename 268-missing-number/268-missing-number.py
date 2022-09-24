class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = len(nums)
        
        for i in range(len(nums)):
            answer += (i - nums[i])
        return answer
        
        
        
# HashMap but it will take O(N) time complexity
#XOR-> bitwise operation      
# Time complexity: O(1)
# Space complexty: O(N)