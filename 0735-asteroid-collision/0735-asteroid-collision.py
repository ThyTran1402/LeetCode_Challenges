class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while len(stack) and asteroid < 0 and stack[-1] > 0:
                #check if both asteroids are equal
                if stack[-1] == -asteroid:
                    stack.pop() # destroy both asteroids
                    break
                elif stack[-1] < -asteroid: #check if the top of the stack is smaller, remove the +asteroid, continue the comparison
                    stack.pop()
                    continue
                elif stack[-1] > -asteroid: #top of the stack is larger, +asteroid is destroyed
                    break
            else:
                stack.append(asteroid)
        return stack
 
#stack-bases approach   
#Time/Space complexity: O(N)-> N is number of asteroids