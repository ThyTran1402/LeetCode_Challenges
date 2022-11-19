# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next #move slow pointer one step forward
            fast = fast.next.next #move fast pointer two steps forward
        return slow
    
#Time complexity: O(N); N is number of nodes in the linkedlist
#Space complexity: O(1)