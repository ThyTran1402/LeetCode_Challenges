"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        leftChild = root
        
        while leftChild.left:
            head = leftChild
            while head:
                #Connection 1
                head.left.next = head.right
                
                #Connection 2
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftChild = leftChild.left 
        return root

#BFS approach            
#Time complexity: O(N)
#Space complexity: O(1)