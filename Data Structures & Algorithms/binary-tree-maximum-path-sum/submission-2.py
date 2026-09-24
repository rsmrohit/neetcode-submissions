# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path = root.val

        # recurse case will take care of parent involvement or not 
        # Going up will always go bad
        # max path keeps track of maximum across

        # mps sets node val to max of left, right
        # then we set max_path = max of max_path and sum of left and right

        def mps(node):
            nonlocal max_path
            if node == None:
                return 0

            # print("Tree: ", node.val)
            
            left = mps(node.left)
            right = mps(node.right)

            # print(node.val, left, right)
            
            max_path = max(max_path, right + left + node.val)
            node.val = max(node.val + left, node.val + right, node.val)

            max_path = max(node.val, max_path)
            return node.val

        mps(root)

        return max_path
