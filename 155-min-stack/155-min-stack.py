class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) # take min of val and the top of our stack if the stack is not empty
        self.minStack.append(val) # add the min value to the minStack
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # get the first value of the stack

    def getMin(self) -> int:
        return self.minStack[-1]  # get the first value of the minStack


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()