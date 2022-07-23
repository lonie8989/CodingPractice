"""
236. Lowest Common Ancestor of a Binary Tree
Medium

10338

285

Add to List

Share
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition
"""

# 1.
# 2.
# 3.
# 4.

# frame
# problem -> a couple minutes
# clarification -> a couple minutes (edge case, input)
# some time to think
# pesudo code with example
# example simulation with the pesudo code
# coding
# manually run with examples
# feed back


# [3,5,1,6,2,0,8,null,null,7,4] p = 6, q = 7
#               3
#            /     \
#           5       1
#       F  / \  T  / \
#         6   2   0   8
#          F / \ T
#           7   4

# DFS - Backtracking 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def LCA(r, n1, n2):
            # object vs None
            # the node itself does not exist
            if not r:
                return None
            
            if r == n1:
                return n1
            
            if r == n2:
                return n2
            
            left = LCA(r.left, n1, n2)
            right = LCA(r.right, n1, n2)
            
            if left and right:
                return r
            
            return left or right
        
        
        return LCA(root, p, q)

#
#[3,5,1,6,2,0,8,null,null,7,4]
# 5,4
# 5
        


