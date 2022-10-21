class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #(character, fre)
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch,1])
            if stack[-1][1] == k:
                stack.pop()
        return ''.join(ch * k for ch, k in stack)
    
#stack based approach
#Time/space complexity: O(N)