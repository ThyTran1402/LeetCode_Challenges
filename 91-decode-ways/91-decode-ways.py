class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i] == "0":
                return 0
            
            result = dfs(i + 1)
            # check double digits between 10-26
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")): 
                result += dfs(i + 2)
            dp[i] = result
            return result
        return dfs(0)
# Time/Space complexity: O(N)      
# recursive DFS; use decision tree to check for number of ways to decode the 2 digits or 1 digits
            