# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        cache = defaultdict(list)

        def inner(level, node):
            nonlocal cache

            if node:
                cache[level].append(node.val)
            else:
                return

            if node.left:
                inner(level+1, node.left)
            if node.right:
                inner(level+1, node.right)
        inner(0, root)
        rm = [cache[i][-1] for i in cache]
        return rm