class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_arr = [amount + 1] * (amount + 1)
        
        dp_arr[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if i - j >= 0:
                    # coin = 4, a = 7 ->dp[7] = 1 + dp[3]
                    dp_arr[i] = min(dp_arr[i], 1 + dp_arr[i-j])
        return dp_arr[amount] if dp_arr[amount] != amount + 1 else -1
    
# Time compelxity: O(amount + len(coins))
# Space complexity: O(amount)