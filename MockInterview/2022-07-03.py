"""
314. Binary Tree Vertical Order Traversal
Medium

2526

269

Add to List

Share
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
 
"""
# root = [3,9,20,null,null,15,7] root = [] output = None
# [[9],[3,15],[20],[7]]
#        [0,node]
#         3
#      [9]  20
#         15   7
# Breath first search.. 
# add the node into the dic: key = vert_layer, value: same layer nodes
# 1. go to left most node -> vert_layer: 1st layer(index)
# 2. check the key in the dic if it's there, then insert into the value list and else make now one
# 3. if node traveral to left
#        then vert_layer--
#       node traversl to right
#        then vert_layer++

from collections import defaultdict, deque

class TreeNode():
    def __init__(self, val=0, right, left):
        self.val = val
        self.right = right
        self.left = left

def BinaryTreeVerticalOrderTraversal(root: TreeNode):
    if not root: return None
    d = collections.defaultdict(list)
    q = collections.deque()
    res = []
    while q:
        size = len(q)
        for _ in range(size):
            x_coor, node = q.popleft()
            d[x_coor].append(node)

            if node.left:
                q.append([x_coor-1, node.left])
            if node.right:
                q.append([x_coor+1, node.right])
    for k, v in d.item():
        res.append([k, v])
    res.sort(key = lambda x: x[0])

    return res.
    
    
                
# practice: BFS -> queue 
                
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return None
        
        d = collections.defaultdict(list) # default dict
        q = collections.deque()
        q.append([0, root])
        
        res = []
        
        while q:

            size = len(q)
            
            for _ in range(size):
                
                score, node = q.popleft()
                d[score].append(node.val)
                
                if node.left:
                    q.append([score - 1, node.left])
                    
                if node.right:
                    q.append([score+1, node.right])
                    
        
        for k, v in d.items():
            res.append([k, v])
            
        
        res.sort(key = lambda x: x[0])
        
        
        return [x[1] for x in res]            
        
    
    


#
#
#
      
