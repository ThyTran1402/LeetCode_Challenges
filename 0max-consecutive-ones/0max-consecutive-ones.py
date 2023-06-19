class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt_ones, max_ones = 0, 0
        #n = len(nums)
        for i in nums:
            if i == 1:
                cnt_ones += 1
            else:
                max_ones = max(max_ones, cnt_ones)
                cnt_ones = 0
        return max(max_ones, cnt_ones)
    
#Time complexity: O(n); n is number of elements in nums
#Space complexity: O(1)