from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        
        dict = {}
        for ch in s:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
                
        heap = []
        for k in dict:
            heappush(heap, (-dict[k], k))
            
        result = ""
        while len(heap) > 1:
            fre1, ch1 = heappop(heap)
            fre2, ch2 = heappop(heap)
            result += ch1
            result += ch2
            
            if abs(fre1) > 1:
                heappush(heap, (fre1+1, ch1))
            if abs(fre2) > 1:
                heappush(heap, (fre2+1, ch2))
                
        if heap:
            fre, char = heap[0]
            if abs(fre) > 1:
                return ""
            else:
                result += char
        return result
    
#use maxheap; we push all letters into maxheap with negative fre
#Time complexity: O(N)
#Space complexity: O(N)