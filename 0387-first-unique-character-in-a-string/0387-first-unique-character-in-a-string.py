class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap_count = {}
        strLength = len(s)
        for i in range(strLength):
            if s[i] in hashMap_count:
                hashMap_count[s[i]] += 1
            else:
                hashMap_count[s[i]] = 1
        for i in range(strLength):
            if hashMap_count[s[i]] == 1:
                return i
        return -1
    
#keep track of the number of occurences of each character in the str
#hash map to store the character as a key and number of occurences in the str
#Time complexity: O(N)
#Space complexity: O(1)