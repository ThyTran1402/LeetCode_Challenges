class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        res = [0] * (n+1)
        res[0] = 1
        return res
    
    
#Add Binary
#Time/Space complexity: O(n); n is the number of elements in the input list

