"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = [node]
        r_dict = {node.val: Node(node.val)}

        while q:
            n = q.pop(0)

            for nbor in n.neighbors:
                # create node if does not exist
                if nbor.val not in r_dict:
                    r_dict[nbor.val] = Node(nbor.val)
                    q.append(nbor)
                
                r_dict[n.val].neighbors.append(r_dict[nbor.val])

        return r_dict[node.val]