class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x%10==0):
            return False
        
        answer = 0
        while x > answer:
            answer = answer * 10 + x % 10
            x //= 10
        return x == answer or x == answer//10
    
#Time complexity: O(N)
#Spacce complexity: O(1)
