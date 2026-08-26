# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        listLinked = []
        curr = head
        
        while curr:
            listLinked.append(curr)
            curr = curr.next
        
        res = head
        l, r = 1, len(listLinked) - 1
        forwardTurn = False
        while l <= r:
            if forwardTurn:
                res.next = listLinked[l]
                l += 1
            else:
                res.next = listLinked[r]
                r -= 1
            forwardTurn = not forwardTurn
            res = res.next
        
        res.next = None
