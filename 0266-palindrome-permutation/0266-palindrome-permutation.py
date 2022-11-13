class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashMap = {}
        idx = 0
        for i in s:
            idx += 1
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        
        count = 0        
        for char in hashMap.keys():
            if hashMap[char] % 2:
                count += 1
            if count > 1:
                return False
        return True
            
#use hashMap to store the frequency of each character and characters
#Time complexity: O(N)
#Space complexity: O(1)