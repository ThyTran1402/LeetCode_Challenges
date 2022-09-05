class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            start, end = i + 1, len(nums) - 1
            while start < end:
                threeSum = a + nums[start] + nums[end]
                if threeSum > 0:
                    end -= 1
                elif threeSum < 0:
                    start += 1
                else:
                    result.append([a, nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
            
        return result
                    
        # [-1, -1, 0, 0, 2, 2]
               
        
# Time complexity: O(NlogN) + O(N^2) = O(N^2)
# Space complexity: O(1)
