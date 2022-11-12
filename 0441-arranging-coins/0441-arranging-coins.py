class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 0, n
        while start <= end:
            k = (start + end) // 2
            current = k*(k+1) // 2
            if current == n:
                return k
            if n < current:
                end = k - 1
            else:
                start = k + 1
        return end
    
#Binary search approach
#Time complexity: O(logN)
#Space complexity: O(1)