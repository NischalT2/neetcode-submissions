"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        curr = head
        curr_new = dummy
        oldToNew = {}

        while curr:
            copy = Node(curr.val)
            curr_new.next = copy
            curr_new = curr_new.next
            oldToNew[curr] = curr_new
            curr = curr.next
        
        curr = head
        curr_new = dummy.next
        while curr_new:
            if curr.random:
                curr_new.random = oldToNew[curr.random]
            curr = curr.next
            curr_new = curr_new.next
        
        return dummy.next