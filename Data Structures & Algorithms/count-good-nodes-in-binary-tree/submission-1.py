# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cash = 0

        def traverse(node, max_v):
            nonlocal cash
            if not node:
                return
            # print(node.val, max_v)

            if max_v <= node.val:
                cash += 1
            
            max_v = max(max_v, node.val)
            traverse(node.right, max_v)
            traverse(node.left, max_v)
        
        traverse(root, root.val-1)
        return cash