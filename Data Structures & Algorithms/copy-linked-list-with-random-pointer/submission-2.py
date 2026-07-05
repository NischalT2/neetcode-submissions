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
        curr = dummy
        nodes = {}

        old = head
        while old:
            new_node = Node(old.val)
            nodes[old] = new_node

            curr.next = new_node
            curr = curr.next
            old = old.next
        
        old2 = head
        while old2:
            if old2.random == None:
                nodes[old2].random = old
            else:
                nodes[old2].random = nodes[old2.random]
            
            old2 = old2.next

        return dummy.next
            
        

