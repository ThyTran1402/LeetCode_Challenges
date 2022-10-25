"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        dummy = Node(0, None, head, None)
        prev = dummy #track the previous node
        stack = []
        stack.append(head) #push head to the stack
        
        while stack:
            cur = stack.pop()
            prev.next = cur
            cur.prev = prev
            
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            prev = cur
        dummy.next.prev = None
        return dummy.next
    
#iterative DFS
#Time/Space complexity: O(N) -> N is the number of nodes in the list