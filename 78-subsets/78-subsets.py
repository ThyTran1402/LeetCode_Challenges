class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] #list
        
        subset = [] #array
        def DFS(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # decison to include nums[i]
            subset.append(nums[i]) # diff subset given to it
            DFS(i + 1) # run DFS on next element
            
            # decision NOT to include nums[i]
            subset.pop() # empty subset given to it
            DFS(i + 1)
            
        DFS(0)
        return result
    
    # brute force: backtracking; visualize decision tree
    # Time complexity: O(N * 2^N)
    # Space complexity: O(N)