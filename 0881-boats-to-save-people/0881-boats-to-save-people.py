class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() #sort the array first
        low, high = 0, len(people)-1
        boats = 0
        
        while low <= high:
            if people[low] + people[high] <= limit: #form a pari-> sit in the same boat
                low += 1
                high -= 1
            else:
                high -= 1
            boats += 1
        return boats
    
#Greedy
#Time complexity: O(NlogN)
#Space complexity: O(N)