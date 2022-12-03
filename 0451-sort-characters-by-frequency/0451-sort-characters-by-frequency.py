from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        freqChar = list(s)
        freqChar.sort(key=lambda x: (counter[x], x), reverse=True)
        return "".join(freqChar)
 
   
#Time complexity: O(NlogN)
#Space complexity: O(N)