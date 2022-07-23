"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# first node = [2], index = 0
# clone = [[2]]
#     find => neighhors
# 
#    if the neighbors empty return visited

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
                
            new_node = Node(node.val, [])
            visited[node] = new_node
            
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
        
            return new_node

        return dfs(node) if node else None
        
            
