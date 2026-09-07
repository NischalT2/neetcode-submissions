# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        arr = []
        

        while q:
            curr = q.popleft()
            arr.append(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        arr = sorted(arr)

        return arr[k - 1]



        """
        Given: a root of a BST
                integer k

        Output: the kth smallest value in the tree (index starts at 1)

        Brute force: go through each node in the BST, store them in an 
        array and then sort it and return that kth value.


        """