"""
133. Clone Graph
Share
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    s;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
"""
##
# 1: the neighbors are 2, 4
# 2: the neighbors are 1, 3
# ...

# [[2,4],[1,3],[2,4],[1,3]]
#   ^ 1st node 
# 1 | (2,4) > (1,2) (1,4) add into deepCopy
# 2 | (1,3) > (2,3) add into deepCopy
# 3 | (2,4) > (3,4) add into deepCopy
# 4 | (1.3)

# create result node
# Node.neighbors 
# if the sudden edge won't in the result node
#     then add as neighebor
# DFS

def deepCopyGraph(node):


class Solution:
    def __init__(self):
        
        self.d = {} #{original Node: copied Node}
    
    def cloneGraph(self, node):
        
        if not node:
            return
        
        if not node in self.d:
            
            # create a new node
            self.d[node] = Node(node.val)
            
            # fill in the neighbors list
            # by creating new nodes
            for nei in node.neighbors:
                self.d[node].neighbors.append(self.cloneGraph(nei))
                
                
        return self.d[node]