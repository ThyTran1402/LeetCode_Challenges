class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        start = end = 0
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest
        return jumps
  
#greedy approach  
#Time complexity: O(N)
#Space complexity: O(1)