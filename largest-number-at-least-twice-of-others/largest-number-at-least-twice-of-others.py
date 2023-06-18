class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_idx = 0
        max1, max2 = -1, -1
        for i, val in enumerate(nums):
            if val > max1:
                max2 = max1
                max1 = val
                max_idx = i
            elif val > max2:
                max2 = val
        if max1 < 2 * max2:
            return -1
        return max_idx
    
#Time complexity: O(n); n is length of nums
#Space complexity: O(1)
        