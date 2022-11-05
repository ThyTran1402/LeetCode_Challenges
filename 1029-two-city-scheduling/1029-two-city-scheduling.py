class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        n = len(costs) // 2
        minCost = 0
        for a_cost, b_cost in costs:
            arr.append(b_cost-a_cost)
            minCost += a_cost
        arr.sort()
        for i in range(n):
            minCost += arr[i]
        return minCost
    
#greedy approach
#Time complexity: O(NlogN)
#Space complexity: O(log N)