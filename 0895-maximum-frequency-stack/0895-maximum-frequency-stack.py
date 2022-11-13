class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int) #frequency hashmap
        self.group = defaultdict(list) #group hashmap
        self.maxFrequency = 0

    def push(self, val: int) -> None:
        freq = self.frequency[val] + 1
        self.frequency[val] = freq
        
        if freq > self.maxFrequency:
            self.maxFrequency = freq
        self.group[freq].append(val)

    def pop(self) -> int:
        val = ""
        if self.maxFrequency > 0:
            val = self.group[self.maxFrequency].pop()
            self.frequency[val] -= 1
            if not self.group[self.maxFrequency]:
                self.maxFrequency -= 1
        else:
            return -1
        return val
    
#Time complexity: O(1) for push() and pop()
#Space complexity: O(N); N is number of elements in freqStack


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()