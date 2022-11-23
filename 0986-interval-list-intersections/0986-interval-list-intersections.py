class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            if start <= end:
                result.append([start, end])
            
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        return result
    
#merge intervals pattern
#Time complexity: O(M+N); M, N are the lengths of firstList and secondList
#Space complexity: O(M+N)