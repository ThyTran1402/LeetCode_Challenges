class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap to count the occurence of each value
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
            
        result = []
        for i in range(len(freq) - 1, -1, -1): # traverse in reverse order
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        
        
# Bucket sort      
# Time/Spacee complexity: O(N)


