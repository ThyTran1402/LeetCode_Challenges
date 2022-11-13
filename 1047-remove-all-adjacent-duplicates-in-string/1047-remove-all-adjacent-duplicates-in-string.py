class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
   
#stack 
#Time complexity: O(N); N is length of s
#Space complexity: O(N-D); D is total length for duplicates
