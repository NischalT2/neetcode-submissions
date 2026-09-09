# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        inorderMap = {}
        for i, val in enumerate(inorder):
            inorderMap[val] = i

        def helper(preStart, inStart, inEnd):
            if inEnd < inStart:
                return None

            rootVal = preorder[preStart]
            root = TreeNode(rootVal)

            mid = inorderMap[rootVal]
            leftSize = mid - inStart

            root.left = helper(preStart + 1, inStart, mid - 1)
            root.right = helper(preStart + leftSize + 1, mid + 1, inEnd)

            return root
        
        return helper(0, 0, len(inorder) - 1)
