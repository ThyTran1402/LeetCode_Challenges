class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def DFS(i, current, total):
            if total == target:
                result.append(current.copy())
                return
                
            if i >= len(candidates) or total > target:
                return
            
            current.append(candidates[i])
            DFS(i, current, total + candidates[i])
            current.pop()
            DFS(i + 1, current, total)
            
        DFS(0, [], 0)
        return result
                
            