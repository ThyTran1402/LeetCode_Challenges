# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB
        while pointerA != pointerB:
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next
        return pointerA
    
    
# two pointers approach
#Time complexity: O(N + M) -> N, M are the length of listA and listB
#Space complexity: O(1)