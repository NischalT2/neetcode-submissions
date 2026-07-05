# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        num1, num2 = l1, l2
        carry = 0
        while num1 and num2:
            sum = num1.val + num2.val + carry
            new = ListNode(sum % 10)
            carry = sum // 10

            curr.next = new
            num1, num2 = num1.next, num2.next
            curr = curr.next
        
        while num1:
            sum = num1.val + carry
            new = ListNode(sum % 10)
            carry = sum // 10
            
            curr.next = new
            num1 = num1.next
            curr = curr.next
        
        while num2:
            sum = num2.val + carry
            new = ListNode(sum % 10)
            carry = sum // 10
            
            curr.next = new
            num2 = num2.next
            curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)

        
        return dummy.next
        