# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        count_nodes = 0
        while not currentNode is None:
            count_nodes += 1
            currentNode = currentNode.next
        idx = count_nodes // 2
        currentNode = head
        for i in range(idx):
            currentNode = currentNode.next
        return currentNode
    
#Time complexity: O(N)
#Space complexity: O(1)
    
