class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        job = sorted(list(zip(startTime, endTime, profit)))
        startTime = [job[i][0] for i in range(n)]
        
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            answer = dp(i+1)
            j = bisect_left(startTime, job[i][1])
            answer = max(answer, dp(j) + job[i][2])
            return answer
        
        return dp(0)
    
#Time complexity: O(NlogN)
#Space complexity: O(1)