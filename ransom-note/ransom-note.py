class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = [0] * 26
        m = len(ransomNote)
        n = len(magazine)
        for i in range(n):
            counts[ord(magazine[i]) - ord('a')] += 1
            
        for i in range(m):
            if (counts[ord(ransomNote[i]) - ord('a')] == 0):
                return False
            
            counts[ord(ransomNote[i]) - ord('a')] -= 1
        return True
                
        