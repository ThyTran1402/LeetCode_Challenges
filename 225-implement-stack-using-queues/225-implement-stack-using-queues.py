class MyStack:

    def __init__(self):
        self.qu = []

    def push(self, x: int) -> None:
        self.qu.append(x)

    def pop(self) -> int:
        return self.qu.pop() # remove element from top of stack and return it

    def top(self) -> int:
        return self.qu[-1] # return element on the top of the stack

    def empty(self) -> bool:
        return len(self.qu) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()