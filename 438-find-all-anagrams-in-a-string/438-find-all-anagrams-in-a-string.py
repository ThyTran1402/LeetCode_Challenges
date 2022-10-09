from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_s, length_p = len(s), len(p)
        
        counter_s = Counter()
        counter_p = Counter(p)
        
        if length_s < length_p:
            return []
        
        result = []
        #sliding window for string s
        for i in range(length_s):
            counter_s[s[i]] += 1 #add one char from the right side of window
            if i >= length_p:
                if counter_s[s[i-length_p]] == 1:
                    del counter_s[s[i-length_p]]
                else:
                    counter_s[s[i-length_p]] -= 1 #remove one char from the left side of window
                    
            if counter_s == counter_p:
                result.append(i-length_p+1)
                
        return result

#sliding window with hashmap                
#Time complexity: N(N_s+N_p) -> O(N_s)
#Space complexity: O(1)