class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        firstHalf = secondHalf = 0
        start, end = 0, len(s)-1
        while start < end:
            firstHalf += s[start] in vowels
            secondHalf += s[end] in vowels
            start += 1
            end -= 1
        return firstHalf == secondHalf

 
#use Hashset   
#Time complexity: O(N)
#Space complexity: O(1)