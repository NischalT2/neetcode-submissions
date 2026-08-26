# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find mid point as well as the end
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse direction to the right of the midpoint
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Reorder
        left, right = head, prev
        while right:
            leftNext, rightNext = left.next, right.next
            left.next = right
            right.next = leftNext

            left, right = leftNext, rightNext


