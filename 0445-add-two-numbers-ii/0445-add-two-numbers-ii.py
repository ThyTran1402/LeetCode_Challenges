# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry, head = 0, None
        while stack1 or stack2 or carry:
            digit1, digit2 = 0, 0
            digit1 = stack1.pop() if stack1 else 0 #pop the last element fron stack and 0 for empty stack
            digit2 = stack2.pop() if stack2 else 0
            carry, digit_num = divmod(digit1+digit2+carry, 10)
            newHead = ListNode(digit_num)
            newHead.next = head
            head = newHead
        return head
    
#use two stacks since we cannot reverse our original lists
#Time/Space complexity: O(N+M)