# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        cur = head
        for _ in range(left - 1):
            cur = cur.next
            prev = prev.next
            
        for _ in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next
  
#iterative linkedlist reversal   
#Time complexity: O(N) -> N is the number of nodes in the linked list
#Space complexity: O(1)
    
