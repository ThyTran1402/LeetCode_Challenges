# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        apiCalls = 0
        while start < end: #search the entire list
            middle = start + (end-start) // 2
            
            if isBadVersion(middle):
                end = middle
            else:
                start = middle + 1
            apiCalls += 1
        return start

#binary search approach   
#Time complexity: O(logN)
#Space complexity: O(1)