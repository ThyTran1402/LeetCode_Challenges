import re
class Solution:
    def remove_spaces(self, s:str) -> list:
        start, end = 0, len(s)-1
        while start <= end and s[start] == ' ':
            start += 1
            
        while start <= end and s[end] == ' ':
            end -= 1

        result = []
        while start <= end:
            if s[start] != ' ':
                result.append(s[start])
            elif result[-1] != ' ':
                result.append(s[start])
            start += 1
        return result
    
    def reverseStr(self, lst: list, start: int, end: int) -> None:
        while start <= end:
            lst[start], lst[end] = lst[end], lst[start]
            start, end = start + 1, end - 1
            
    def reverse_each_word(self, lst: list)->None:
        n = len(lst)
        start = end = 0
        while start < n:
            while end < n and lst[end] != ' ':
                end += 1
            self.reverseStr(lst, start, end-1)
            start = end + 1
            end += 1
    
    def reverseWords(self, s: str) -> str:
        lst = self.remove_spaces(s)
        
        self.reverseStr(lst, 0, len(lst)-1) #reverse the whole str
        self.reverse_each_word(lst) #reverse each word
        return ''.join(lst)
        
              
#Two pointers: 1.reverse the string, 2.Traverse the string, and reverse each word
#Time complexity: O(N)
#Space complexity: O(N)
        