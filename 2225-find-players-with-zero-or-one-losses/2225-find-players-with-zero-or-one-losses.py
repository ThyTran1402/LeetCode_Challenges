class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashtable, winner, loser = {}, [], []
        for w, l in matches:
            hashtable[w] = hashtable.get(w, 0)
            hashtable[l] = hashtable.get(l, 0) + 1
        for key, value in hashtable.items():
            if value == 0:
                winner.append(key)
            if value == 1:
                loser.append(key)
        return [sorted(winner), sorted(loser)]
    
#use Hashmap
#Time complexity: O(NlogN)
#Space complexity: O(N)