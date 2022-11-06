class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = nums[0]
        count = 0
        for number in nums:
            if number == majority_element:
                count += 1
            elif count == 0:
                majority_element = number
                count = 1
            else:
                count -= 1
        return majority_element
    
#Boyer Moore Voting Algo
#Time complexity: O(N)
#Space complexity: O(1)