class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        dict = defaultdict(int)
        for i in range(n-9):
            dict[s[i:i+10]] += 1
            
        result = []
        for key, value in dict.items():
            if value >= 2:
                result.append(key)
        return result
    
#use hashMap to store the frequency of all possible substring with length 10
#return all substring which occur more than once
#Time complexity: O(N)
#Space complexity: O(N)