from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        countLosses = defaultdict(int)
        for winner, loser in matches:
            countLosses[winner] = countLosses.get(winner, 0)
            countLosses[loser] = countLosses.get(loser, 0) + 1

        oneLost, zeroLost = [], []
        for player, cnt in countLosses.items():
            if cnt == 0:
                zeroLost.append(player)
            if cnt == 1:
                oneLost.append(player)
        return [sorted(zeroLost), sorted(oneLost)]

#HashMap
#Time complexity: O(nlogn); n is length of matches
#Space complexity: O(n)


