class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        current_length, result = 0, []
        current_line = []
        
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                for i in range(maxWidth - current_length):
                    current_line[i % max(len(current_line) - 1, 1)] += ' '
                result.append(''.join(current_line))
                current_line, current_length = [], 0
            current_line.append(word)
            current_length += len(word)
            
        # Use ljust(L) to pad the last line with the appropriate number of blanks
        return result + [' '.join(current_line).ljust(maxWidth)]
    
    
#Time complexity: O(N)
#Space complexity: O(N)