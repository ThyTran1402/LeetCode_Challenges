class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stack(s):
            stack = []
            
            for i in s:
                if i != "#":
                    stack.append(i)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return stack(s) == stack(t)
    
# Build String -> use stack approach
# Time comlexity: O(N+M) -> M,N are the length of s and t
# Space complexity: O(N+M)