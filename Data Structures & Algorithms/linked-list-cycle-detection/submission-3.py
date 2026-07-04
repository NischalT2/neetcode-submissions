# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single = head
        double = head

        while double and double.next:
            double = double.next.next
            single = single.next

            if double == single:
                return True
        
        return False
