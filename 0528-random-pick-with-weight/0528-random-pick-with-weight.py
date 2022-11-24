import random
class Solution:
    def __init__(self, w: List[int]):
        self.cum_sums = []
        cum_sum = 0
        
        for weight in w:
            cum_sum += weight
            self.cum_sums.append(cum_sum)
        self.totalSum = cum_sum

    def pickIndex(self) -> int:
        target = self.totalSum * random.random()
        
        start = 0
        end = len(self.cum_sums)
        while start < end:
            middle = start + (end-start) // 2
            if target > self.cum_sums[middle]:
                start = middle + 1
            else:
                end = middle
        return start


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()