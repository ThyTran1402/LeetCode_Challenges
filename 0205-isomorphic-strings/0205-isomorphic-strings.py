class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = [0 for _ in range(256)]
        dict2 = [0 for _ in range(256)]
        
        for i in range(len(s)):
            if dict1[ord(s[i])] != dict2[ord(t[i])]:
                return False
            dict1[ord(s[i])] = i + 1
            dict2[ord(t[i])] = i + 1
        return True
    
#use Hashmap to map directly 'e'->'a, 'g'->'d', 'g'->'d'
#mark the char with the same value 'e'->1, 'a'->1, 'g'->2, 'd'->2
#Time complexity: O(N)
#Space complexity: O(1)