class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        return sum(s in jewels for s in stones) #way 3
 
#use hashset       
#Time complexity: O(J+S) -> J, S are the lengths of jewels and stones
#Space complexity: O(J)