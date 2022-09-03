class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0]) # sort by the start value
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd= result[-1][1]
            
            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])
        return result
                
            # [1, 5], [2, 4] = [1, 5]
            
# Time complexity: O(NlogN)
# Space complexity: O(logN)