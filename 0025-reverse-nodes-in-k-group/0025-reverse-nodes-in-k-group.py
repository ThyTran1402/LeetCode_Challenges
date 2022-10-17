# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # 1 -> 2 -> 3
        # 1 -> 3 -> 2
        groupPrev = dummy
        
        while True:
            kthNode = self.getKthNode(groupPrev, k) #kthNode is the last node in our group
            if not kthNode:
                break
            groupNext = kthNode.next
            #reverse group
            prev, current = kthNode.next, groupPrev.next
            while current != groupNext:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
        
            temp = groupPrev.next #First node in our group
            groupPrev.next = kthNode
            groupPrev = temp
        return dummy.next
            
    
    def getKthNode(self, current, k):
        while current and k > 0:
            current = current.next # update current
            k -= 1
        return current
    
#Time complexity: O(N)
#Space complexity: O(1)