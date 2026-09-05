# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []    
        q = deque([root])

        while q:
            level_len = len(q)
            curr = []
            for i in range(level_len):
                curr_node = q.popleft()
                if curr_node:
                    curr.append(curr_node.val)
                    q.append(curr_node.left)
                    q.append(curr_node.right)
            
            if curr:
                res.append(curr)
        
        return res

            

                