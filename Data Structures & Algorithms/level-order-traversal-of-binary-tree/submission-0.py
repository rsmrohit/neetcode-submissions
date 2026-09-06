# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        l_l = []

        if not root:
            return []

        def traverse(lvl, node):
            nonlocal l_l
            if len(l_l) == lvl:
                l_l.append([node.val])
            else:
                l_l[lvl].append(node.val)
            
            if node.left:
                traverse(lvl+1, node.left)
            if node.right:
                traverse(lvl+1, node.right)
        
        traverse(0, root)

        return l_l