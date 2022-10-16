class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        
        for number in nums:
            xor ^= number
        return xor
    

# bit manipulation approach-> use XOR
# A    B    A^B
# 0    0    0
# 0    1    1
# 1    0    1
# 1    1    1
# Time complexity: O(N)
# Space complexity: O(1)