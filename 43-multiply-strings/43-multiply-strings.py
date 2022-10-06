class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        multiply = [0] * (len(num1) + len(num2))
        position = len(multiply) - 1
        
        for i in reversed(num1):
            tempPosition = position
            for j in reversed(num2):
                multiply[tempPosition] += int(i) * int(j)
                multiply[tempPosition - 1] += multiply[tempPosition] // 10
                multiply[tempPosition] %= 10
                tempPosition -= 1
            position -= 1
            
        point = 0
        while point < len(multiply) - 1 and multiply[point] == 0:
            point += 1
        return ''.join(map(str, multiply[point:]))
    