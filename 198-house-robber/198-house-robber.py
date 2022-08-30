class Solution:
    def rob(self, nums: List[int]) -> int:
        robber1, robber2 = 0, 0
        
        # [robber1, robber2, n, n+1, ...]
        for n in nums:
            temp = max(n + robber1, robber2)
            robber1 = robber2
            robber2 = temp
        return robber2
        
# Time/Space complexity: O(N)