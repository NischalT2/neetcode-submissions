# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        counter = 0
        req = length - n
        new = head
        prev = None
        while new and counter < req:
            prev = new
            new = new.next
            counter += 1
        
        if req == 0:
            return head.next

        prev.next = new.next
        
        return head


        