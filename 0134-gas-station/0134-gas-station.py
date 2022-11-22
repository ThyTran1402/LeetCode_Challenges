class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_gas, start_idx = 0, 0
        for i in range(len(gas)):
            total_gas = total_gas + (gas[i] - cost[i])
            
            if total_gas < 0:
                total_gas = 0
                start_idx = i + 1
        return start_idx
    
#greedy approach
#Time complexity: O(N)
#Space complexity: O(1)