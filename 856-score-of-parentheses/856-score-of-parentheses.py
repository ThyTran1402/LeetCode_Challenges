class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        current = 0
        for i in s:
            if i == '(':
                stack.append(current)
                current = 0 # reset current = 0
            else: # if i == ')
                current += stack.pop() + max(current, 1) # current will be doubled and at least 1
        return current
    
#stack approach
#Time complexity: O(N) -> N is the length of s
#Space complexity: O(N) -> size of the stack
                