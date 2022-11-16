class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return checkPalindrome(s, left, right-1) or checkPalindrome(s, left+1, right)
            left += 1
            right -= 1
        return True
    
#two Pointers with helper function checkPalindrome
#Time complexity: O(N)
#Space complexity: O(1)