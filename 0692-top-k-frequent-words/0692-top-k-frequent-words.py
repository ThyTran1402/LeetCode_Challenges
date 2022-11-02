from collections import Counter
from heapq import heappush, heappop

class Pair:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency
        
    def __lt__(self, other):
        return self.frequency < other.frequency or (self.frequency == other.frequency and self.word > other.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for word, frequency in count.items():
            heappush(heap, Pair(word, frequency))
            if len(heap) > k:
                heappop(heap)
        return [other.word for other in sorted(heap, reverse=True)]
 
#Min heap approach   
#Time complexity: O(NlogK)->O(N)+O(Nlogk)+O(klogk) = O(NlogK); N is length of words
#Space complexity: O(N)