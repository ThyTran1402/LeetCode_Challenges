class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^-n = 1 / x^n
        
        def baseCase(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            result = baseCase(x * x, n // 2)
            # result = result * result
            return x * result if n % 2 else result
            
        result = baseCase(x, abs(n))
        return result if n >= 0 else 1/ result

# recurive: divide and conquer to break down the exponetial into smaller one
# log(n)-> how many times can we divide the number n
# Time complexity: O(logN)
# Space complexity: O(logN)