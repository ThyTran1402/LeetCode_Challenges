class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # base case
        if (len(nums) == 1):
            return  [nums[:]]
        
        for i in range(len(nums)):
            number = nums.pop(0) # pop out the first element
            permutations = self.permute(nums)
            
            # [2, 3, 1], [3, 2, 1]
            for permutation in permutations:
                permutation.append(number)
            result.extend(permutations)
            nums.append(number)
            
        return result