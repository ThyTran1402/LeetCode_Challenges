class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        #minRooms = 0
        freeRooms = []
        
        heapq.heappush(freeRooms, intervals[0][1])
        for i in intervals[1:]:
            if freeRooms[0] <= i[0]:
                heapq.heappop(freeRooms)
            heapq.heappush(freeRooms, i[1])
        return len(freeRooms)
            
            
#use minHeap to keep track of the ending time of all meetings currently happpening
#so that when we schedule a new meeting, we can see what meetings alreaady ended.
#Time complexity: O(NlogN) -> we have to sort the meetings
#Space complexity: O(N), N is the number of meetings