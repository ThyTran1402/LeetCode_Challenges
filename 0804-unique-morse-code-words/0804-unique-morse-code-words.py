class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hashset = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        result = []
        for w in words:
            result.append("".join(hashset[ord(c)-ord('a')] for c in w))
        return len(set(result)) # return the size of the set
    
    
#hashset; transformation in to a set result
#Time/Space complexity: O(N*K)-> N is the number of words, K average is the length of each word