class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        modulo = collections.defaultdict(int) # record the frequency of the remainder
        result = 0
        for t in time:
            if t % 60 == 0:
                result += modulo[0]
            else:
                result += modulo[60-t%60]
            modulo[t%60] += 1 # update the frequency of remainder
        return result
    
#use array to store the frequency of remainder
#Time complexity: O(N)
#Space complexity: O(1)