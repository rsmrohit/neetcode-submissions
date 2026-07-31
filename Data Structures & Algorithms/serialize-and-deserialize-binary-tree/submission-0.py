# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        capture = []
        def serial(node):
            nonlocal capture
            if not node:
                capture += ["None"]
                return
            
            capture += [str(node.val)]
            serial(node.left)
            serial(node.right)
            # return capture + [node.val] + serial(node.left) + serial(node.right)

        serial(root)
        return ",".join(capture)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')

        def deserial():
            d = data.pop(0)
            if d == "None":
                return None
            node = TreeNode(int(d))
            node.left = deserial()
            node.right = deserial()
            return node

        return deserial()

