class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        lcp = min(strs, key = len)
        for i, char in enumerate(lcp):
            for c in strs:
                if c[i] != char:
                    return lcp[:i]
        return lcp
    
    
#Time complexity: O(N)
#Space complexity: O(1)