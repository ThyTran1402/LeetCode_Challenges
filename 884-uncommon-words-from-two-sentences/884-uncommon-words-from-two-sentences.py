class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = collections.Counter((s1 + " " + s2).split())
        return [word for word in count if count[word] == 1]
    
    
# Time/spacee complexity: O(M + N) -> M and N are the lengths of s1 and s2