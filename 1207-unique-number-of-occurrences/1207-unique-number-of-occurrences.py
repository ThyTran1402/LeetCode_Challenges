class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = {}
        
        for i in arr:
            if i not in dictionary:
                dictionary[i] =0 
            dictionary[i] += 1
        return len(dictionary) == len(set(dictionary.values()))
    
#Time/Space complexity: O(N)