import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count_cards = collections.Counter(hand)
        
        while count_cards:
            minCard = min(count_cards)
            for i in range(minCard, minCard + groupSize):
                v = count_cards[i]
                if not v: return False
                if v == 1:
                    del count_cards[i]
                else:
                    count_cards[i] = v-1
        return True
    
#use heap to store the count of each card