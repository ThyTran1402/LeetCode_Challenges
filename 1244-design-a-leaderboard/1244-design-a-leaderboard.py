from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self):
        self.scores= defaultdict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0 
        self.scores[playerId] += score      
        
#Time complexity: O(1)
#Space complexity: O(N) 
        

    def top(self, K: int) -> int:
        values = [v for _, v in sorted(self.scores.items(), key = lambda item: item[1])]
        values.sort(reverse=True)
        total_scores, i = 0, 0
        while i < K:
            total_scores += values[i]
            i += 1
        return total_scores
    
#Time complexity: O(1)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        
#Time complexity: O(NlogN)
#Space complexity: O(N)




# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)