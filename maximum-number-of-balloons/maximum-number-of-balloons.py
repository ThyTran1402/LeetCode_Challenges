class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        pattern = {"b": 0, "a": 0, "l": 0, "l": 0, "o": 0, "o": 0, "n": 0}
        for ch in text:
            if ch in pattern:
                pattern[ch] += 1
                #print(pattern[ch])
            
        pattern["l"] //= 2
        #print(pattern["l"])
        pattern["o"] //= 2
        #print(pattern.values())
        return min(pattern.values())
        