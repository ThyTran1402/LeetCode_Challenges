class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        result = []
        
        def backtrack(i, currentStr):
            if len(currentStr) == len(digits):
                result.append(currentStr)
                return
            
            for char in dict[digits[i]]:
                backtrack(i + 1, currentStr + char)
                
        if digits:
            backtrack(0, "")
        return result
    
# recusive backtracking
# Time complexity: O(N * 4^N)
# Space complexity: O(N)