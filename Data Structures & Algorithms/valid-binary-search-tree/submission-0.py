# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            curr, low, high = q.popleft()
            
            if not low < curr.val < high:
                return False
            
            if curr.left:
                q.append((curr.left, low, curr.val))
            if curr.right:
                q.append((curr.right, curr.val, high))
        
        return True

