class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numeral = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        result, i = "", 0
        while num:
            result += (num//value[i]) * roman_numeral[i]
            num %= value[i]
            i += 1
        return result
    
  
#Greedy approach  
#Time/Space complexity: O(1)