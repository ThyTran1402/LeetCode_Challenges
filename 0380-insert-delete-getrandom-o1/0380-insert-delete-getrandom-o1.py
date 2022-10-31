import random
class RandomizedSet:

    def __init__(self):
        self.numbers = []
        self.positions = {}

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        self.positions[val] = len(self.numbers)
        self.numbers.append(val) #insert a value into the set
        return True # if the set did not contain specified element
    
#Time complexity: O(1)
#Space complexity: O(N) -> N is number of element in the array

    def remove(self, val: int) -> bool:
        if val in self.positions:
            lastElement, idx = self.numbers[-1], self.positions[val]
            self.numbers[idx], self.positions[lastElement] = lastElement, idx
            self.numbers.pop() #delete the last element
            del self.positions[val]
            return True
        return False
    
#Time complexity: O(1)
#Space complexity: O(N)

    def getRandom(self) -> int:
        #get random element from the set
        
        return self.numbers[random.randint(0, len(self.numbers)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()