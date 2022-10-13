# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode1 = evenHead = ListNode(0)
        dummyNode2 = oddHead = ListNode(0)
        
        while head:
            oddHead.next = head
            evenHead.next = head.next
            oddHead = oddHead.next
            evenHead = evenHead.next
            head = head.next.next if evenHead else None
            
        oddHead.next = dummyNode1.next
        return dummyNode2.next
    

# Two pointers at head and tail of the linkedlist
#Time complexity: O(N)
#Space complexity: O(1)