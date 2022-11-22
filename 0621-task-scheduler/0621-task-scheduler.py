class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        fre = [0] * 26 #keep track frequency of each task
        for task in tasks:
            fre[ord(task)-ord('A')] += 1
            
        fre.sort()
        fre_max = fre.pop() #max frequency
        idle = (fre_max-1) * n
        
        while fre and idle > 0:
            idle -= min(fre_max-1, fre.pop())
        idle = max(0, idle) 
        return len(tasks) + idle #busy slots + idle slots
    
#greedy
#Time complexity: O(N)
#Sapce complexity: O(1)  