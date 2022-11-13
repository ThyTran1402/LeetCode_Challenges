class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_char = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove_char[i] = ''
        while stack:
            remove_char[stack.pop()] = ''
        return ''.join(remove_char)
    
#convert s into a list because removing the char takes O(1) and using stack of indexes
#to make sure it's easy to remove '('
#Time/Space complexity: O(N)