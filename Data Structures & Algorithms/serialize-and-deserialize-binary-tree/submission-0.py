# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.val_idx = 0

        def dfs():
            if vals[self.val_idx] == "N":
                self.val_idx += 1
                return None
            
            curr_node = TreeNode(int(vals[self.val_idx]))
            self.val_idx += 1
            curr_node.left = dfs()
            curr_node.right = dfs()
            return curr_node

        return dfs()
