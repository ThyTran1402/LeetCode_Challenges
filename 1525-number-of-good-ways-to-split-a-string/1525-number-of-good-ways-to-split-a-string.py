class Solution:
    def numSplits(self, s: str) -> int:
        left_count = collections.Counter()
        right_count = collections.Counter(s)
        
        result = 0
        for ch in s:
            left_count[ch] += 1
            right_count[ch] -= 1
            if right_count[ch] == 0:
                del right_count[ch]
            
            if len(left_count) == len(right_count):
                result += 1
        return result
    
#left_count and right_count to keep track of the frequency of letters for left and right partitions
#Time complexity: O(N)
#Space complexity: O(1)