from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        length1, length2 = len(word1), len(word2)
        
        if length1 != length2:
            return False
        
        countChar1 = Counter(word1)
        countChar2 = Counter(word2)
        
        for char in countChar1.keys():
            if char not in countChar2.keys():
                return False
            
        fre1 = Counter(countChar1.values())
        fre2 = Counter(countChar2.values())
        
        #check if the frequency counts is the same
        for fre, value in fre1.items():
            if fre2[fre] != value:
                return False
        return True
    
#Time complexity: O(N)
#Space complexity: O(1)