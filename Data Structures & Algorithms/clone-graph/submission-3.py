"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:        
        # visited = set()
        q = []
        r_dict = {}

        root = None

        if node:
            root = Node()
            q.append(node)
            root.val = node.val
            r_dict[root.val] = root

        while q:
            
            n = q.pop(0)

            for nbor in n.neighbors:

                # create node if does not exist
                if nbor.val not in r_dict:
                    r_dict[nbor.val] = Node(nbor.val)
                    q.append(nbor)
                
                r_dict[n.val].neighbors.append(r_dict[nbor.val])    # add node as neighbor

                # if nbor.val not in visited:
                #     q.append(nbor)  # put in q if not done 

            # visited.add(n.val) # finished add to visited

        return root

                
