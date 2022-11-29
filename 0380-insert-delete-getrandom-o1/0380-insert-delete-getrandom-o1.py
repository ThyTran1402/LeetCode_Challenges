from random import choice

class RandomizedSet:

    def __init__(self):
        self.index = {} #hashMap
        self.store = [] #array

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        #insert the actual value as a key and its index as a value
        self.index[val] = len(self.store)
        #append new value to array
        self.store.append(val)
        return True
    
#Time complexity: O(1)
#Space complexity: O(N) -> N is number of element in the array

    def remove(self, val: int) -> bool:
        if val in self.index:
            last, i = self.store[-1], self.index[val]
            self.store[i], self.index[last] = last, i
            #delete the last element
            del self.index[val]
            self.store.pop()
            return True
        return False
    
#Time complexity: O(1)
#Space complexity: O(N)

    def getRandom(self) -> int:
        #get random element from the set
        
        return choice(self.store)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()