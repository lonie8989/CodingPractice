"""
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
                3
               / \
            t 5   1 v
            /  \ / \
           6   2 0  8
               /\
             v7  4v
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
"""
# target is always in the tree
# k = 0? should? target is self 
# k = inf then return []
# input? root of the tree
# output? list[int]
# node object 

# 0. DFS to find the target val and BSF for collect all nodes for k th layers nodes

# first, create graph with key == node.val and value == distance from root
# second, find the target and check that in the graph 
# third, find abs value of the distance + or - k append the node.val to list of res   

def Node(self, val=0, right: Node, left: Node):
    self.val = val
    self.right = right
    self.left = left

def distanceKInBinaryTrees(root: Node, target: int, k: int) -> list[int]:
    if k == 0: return [root.val]
    
    res = []
    graph = {(root.val, 0)} # key: node.val and value: distance from root

    def createGraph(root, d):
        if not root: return
        graph[root.val].append(d)
        if root.right: createGraph(root.right, d+1)
        if root.left: createGraph(root.left, d+1)
    
    createGraph(root, 0)

    def dfs(root, target, k):
        if root.val == target:
            # check the graph
            graph[root.val] 
        if root.right: dfs(root.right, target, k)
        if root.left: dfs(root.left, target, k)
        
        
        
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.g = collections.defaultdict(list)
        self.visited = set()
        self.output = []
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # {5:[3,6,2], 3:[5,1]....} undirected graph
        if not root:
            return self.output
        def DFS(node):
            if not node:
                return
            if node.left:
                self.g[node.val].append(node.left.val)
                self.g[node.left.val].append(node.val)
                DFS(node.left)
            if node.right:
                self.g[node.val].append(node.right.val)
                self.g[node.right.val].append(node.val)
                DFS(node.right)
                
        DFS(root)
        
        targetVal = target.val
        
        q = collections.deque()
        q.append(targetVal)
        self.visited.add(targetVal)
        
        cnt = 0
        while q:
            
            size = len(q)
            cnt = cnt + 1
            for _ in range(size):
                node = q.popleft()
                
                if cnt == k + 1: # cnt - 1 == k
                    self.output.append(node)
                
                for nei in self.g[node]:
                    if nei not in self.visited:
                        q.append(nei)
                        self.visited.add(nei)
        
        return self.output
      