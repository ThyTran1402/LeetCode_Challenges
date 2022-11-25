class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        dp = [0] * len(arr)
        stack = [0]
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            dp[i] = dp[j] + (i-j)*arr[i]
            stack.append(i)
        return sum(dp) % (10**9+7)
  
#monitonic stack  
#Time/Space complexity: O(N)

