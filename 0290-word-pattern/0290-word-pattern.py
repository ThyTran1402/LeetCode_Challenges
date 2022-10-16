class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, words_to_pattern = s.split(' '), dict()
        
        if len(pattern) != len(words):
            return False
        if len(set(pattern)) != len(set(words)):
            return False
        
        for i in range(len(words)):
            if words[i] not in words_to_pattern:
                words_to_pattern[words[i]] = pattern[i]
            elif words_to_pattern[words[i]] != pattern[i]:
                return False
        return True
    
#use hashmap to map words to letters from pattern
#Time complexity: O(N)
#space complexity: O(N)