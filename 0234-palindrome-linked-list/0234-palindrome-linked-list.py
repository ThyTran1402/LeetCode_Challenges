# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next   
        prev = slow
        slow = slow.next
        prev.next = None
        
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True 
    
        
#fast and slow pointers
#Time complexity: O(N)
#Space complexity: O(1)
    
        
#fast and slow pointers
#Time complexity: O(N)
#Space complexity: O(1)
        
    
        

            