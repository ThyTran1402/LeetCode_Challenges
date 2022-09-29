class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start = start + 1 # move to the right one step
            end = end - 1 # move to the left one step
              
        
        
#Two pointer approach
#Time complexity: O(N)
#Space complexity: O(1)
