class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = set()
        for char in s:
            if char not in hashset:
                hashset.add(char)
            else:
                hashset.remove(char)
        return len(s) - len(hashset) + 1 if len(hashset) > 0 else len(s)
    
#HashSet
#Time complexity: O(N)
#Space complexity: O(1)