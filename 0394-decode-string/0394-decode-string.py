class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentStr = ""
        currentK = 0
        
        for ch in s:
            if ch == "[":
                stack.append(currentStr)
                stack.append(currentK)
                currentStr = ""
                currentK = 0
            elif ch == "]":
                lastK = stack.pop()
                lastStr = stack.pop()
                currentStr = lastStr + lastK * currentStr
            elif ch.isdigit():
                currentK = currentK * 10 + int(ch)
            else:
                currentStr += ch
        return currentStr
    
#stack approach
#Time complexity: O(maxK*n), maxK is the maximum value of k, n is the length of s
#Space complexity: O(m+n), m is number of letters (a-z), n is number of digits (0-9)
                