class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        
        result = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = 0
                if diff in dp[j]:
                    count = dp[j][diff]
                    
                dp[i][diff] += dp[j][diff] + 1
                result += count
        return result
                
#Time complexity: O(N^2); N is number of elements in the array
#Space complexity: O(N^2)