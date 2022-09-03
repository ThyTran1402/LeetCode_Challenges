class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                answer.append(newInterval)
                return answer + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # check if the start value of the new interval is greater than the end value of the current interval
                answer.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        answer.append(newInterval)
        return answer
    
# Time/Space compleixity: O(N)