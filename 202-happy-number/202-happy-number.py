class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set() # hashset
        
        while n not in hashset:
            hashset.add(n)
            n = self.sumOfSquares(n)
            
            if n == 1:
                return True
        return False
            
    def sumOfSquares(self, n:int) -> int:
        result = 0
        
        while n: # n is not 0
            digit = n % 10
            digit = digit ** 2 # square the digit
            result += digit
            n = n // 10 # find the next digit
        return result