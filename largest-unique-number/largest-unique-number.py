from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        countFre = defaultdict(int)
        for num in nums:
            countFre[num] += 1
            
        ans = -1
        for num, cnt in countFre.items():
            if cnt == 1:
                ans = max(ans, num)
        return ans
                